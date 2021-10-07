from re import I

from github import Github
import requests
import json
from scanner import scan_diff
from rules import read_rules


# Github API: https://docs.github.com/en/rest/reference/repos#create-a-commit-comment
def leave_comment_on_commit( token, commit_url, path, position, comment ):
    org = commit_url.split('/')[3]
    repo = commit_url.split('/')[4]
    commit_hash = commit_url.split('/')[6]
    api_url = 'https://api.github.com/repos/' + org + '/' + repo + '/commits/' + commit_hash + '/comments'
    print(api_url)
    payload = {'body': comment, 'path': path, 'position':position}
    headers = {'user-agent': 'hcss', 'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token ' + token }
    r = requests.post(api_url, data=json.dumps(payload), headers=headers)



# example: leave_comment_on_commit( token, 'https://github.com/High-Confidence-Security-Tools/hcss/commit/a259de4a63c23b25160baefa2fcdf727aae2a5bf', "src/hcss.py", 5, "donkey chicken" )


def process_single_commit( token, commit_url ):
    """ 
    Process a single commit

    Review all the changes within a single commit and report any findings

    Parameters:
        token (string): Github token
        commit_url (string): URL to the commit

    Returns:
        list: Containing all results
    """

    # print(commit)
    diff_url = commit_url + ".diff"
    print(diff_url)
    headers = {'user-agent': 'hcss', 'Authorization': 'token ' + token }
    r = requests.get( diff_url, headers=headers )
    diff_text = r.text
    if len(diff_text) < 1048576:
        results = scan_diff( r.text )
        for result in results:
            result["commit_url"] = commit_url
    else:
        print("Diff is huge, will skip this one")
    print("----------------------------------------")
    return results



def process_repo( token, repo ):
    """ 
    Process a Github Repo

    Iterate through the commits looking for keys

    Parameters:
    token (string): Github token
    repo (string): Name of repository

    Returns:
    list: Containing all results
    """


    # login to github with our token
    g = Github(token)

    if repo == None:
        # We're going to grab the first repo for this user.
        print("No repo provided, sorry can't help you.")
        sys.exit()
    else:
        repo = g.get_repo(repo)

    # rules = read_rules()
    # print("Rules loaded.")

    all_results = []
    for commit in repo.get_commits( ):
        # print(commit)
        results = process_single_commit( token, commit.html_url )
        all_results = all_results + results
    return all_results


