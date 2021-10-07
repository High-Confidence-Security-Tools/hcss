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

def process_repo( webhook ):
    commits = []
    try:
        webhook_commits = webhook['push']['changes'][0]['commits']
        for webhook_commit in webhook_commits:
            commits.append({
                'id': webhook_commit['hash'],
                'author_id': webhook_commit['author']['user']['account_id'],
                'diff_url': webhook_commit['links']['diff']['href']
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
                result["commit_url"] = commit['diff_url']
                all_results.append(result)
        else:
            print("Diff is huge, will skip this one")
        print("----------------------------------------")
    return all_results
