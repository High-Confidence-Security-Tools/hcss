from os import environ

import requests

from scanner import scan_diff


def retrieve_auth():
    try:
        bitbucket_username = environ['BITBUCKET_USERNAME']
        bitbucket_password = environ['BITBUCKET_PASSWORD']
    except KeyError as err:
        raise SystemExit(f'ERROR: Required env variable not set ({err})')
    return bitbucket_username, bitbucket_password


def leave_comment_on_commit( bitbucket_username, bitbucket_password, repo_full_name, commit_hash, path, position, comment ):
    # https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Bworkspace%7D/%7Brepo_slug%7D/commit/%7Bcommit%7D/comments#post
    api_url = f'https://api.bitbucket.org/2.0/repositories/{repo_full_name}/commit/{commit_hash}/comments'
    payload = {
        "content": { "raw": comment },
        "inline": { "path":  path, "to": position }
    }
    response = requests.post(api_url, json=payload, auth=(bitbucket_username, bitbucket_password))
    try:
        response.raise_for_status()
    except requests.RequestException as err:
        print(f'ERROR: Failed to post comment on commit {err}')


def process_repo( webhook ):
    commits = []
    try:
        webhook_commits = webhook['push']['changes'][0]['commits']
        for webhook_commit in webhook_commits:
            commits.append({
                'hash': webhook_commit['hash'],
                'author_id': webhook_commit['author']['user']['account_id'],
                'diff_url': webhook_commit['links']['diff']['href'],
            })
    except KeyError as err:
        raise SystemExit(f'ERROR: Key missing in bitbucket webhook payload ({err})')

    bitbucket_username, bitbucket_password = retrieve_auth()
    all_results = []
    for commit in commits:
        resp = requests.get(commit['diff_url'], auth=(bitbucket_username, bitbucket_password))
        diff_text = resp.text
        if len(diff_text) < 1048576:

            results = scan_diff(diff_text)
            for result in results:
                result["commit_hash"] = commit['hash']
                all_results.append(result)
        else:
            print("Diff is huge, will skip this one")
        print("----------------------------------------")

    if all_results != []:
        repo_full_name = webhook['repository']['full_name']

        print("--------- inline comment happening on results ----")
        for result in all_results:
            # leave inline comments
            commit_hash = result["commit_hash"]
            path = result["file"][2:]   # the diff starts out with "b/", so remove that part
            position = result["position"]
            comment = "Good Lord, do you realise what you have done?!  Please do not commit secrets to source code repositories!  You better revoke this right now, as I promise you that people seeing this are in the process of hacking it!"
            leave_comment_on_commit( bitbucket_username, bitbucket_password, repo_full_name, commit_hash, path, position, comment )

    return all_results
