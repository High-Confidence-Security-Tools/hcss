from re import I

from github import Github
import requests

from scanner import scan_diff
from rules import read_rules

def process_single_commit( token, commit_url ):

    # print(commit)
    diff_url = commit_url + ".diff"
    print(diff_url)
    # TODO: token will need to be sent in to access private git repos
    r = requests.get( diff_url )
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

