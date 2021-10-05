from re import I

from github import Github
import requests

from scanner import scan_diff
from rules import read_rules

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
        print("No repo provided, so I'll choose a repo from this user")
        repo = g.get_user().get_repos()[0]
    else:
        repo = g.get_repo(repo)

    # rules = read_rules()
    # print("Rules loaded.")

    all_results = []
    for commit in repo.get_commits( ):
        # print(commit)
        diff_url = commit.html_url+".diff"
        print(diff_url)
        r = requests.get( diff_url )
        diff_text = r.text
        if len(diff_text) < 1048576:
            # results = scan_diff( r.text, rules )
            results = scan_diff( r.text )
            # TODO: insert commit URL into each result
            for result in results:
                result["commit_url"] = commit.html_url
            all_results = all_results + results
        else:
            print("Diff is huge, will skip this one")
        print("----------------------------------------")
    return all_results
