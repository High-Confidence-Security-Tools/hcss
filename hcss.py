import os
import sys
from github import Github
import requests
import json
import re


def read_rules( rulesfile ):
    with open(rulesfile, 'r') as f:
        rules = json.loads( f.read() )
    # print( json.dumps(rules, indent=2) )
    return rules


def scan_line( filename, line, rules ):
    for rule in rules["rules"]:
        match = re.search(rule["regex"], line)
        if match:
            print("*************************************************************")
            print("Found " + rule["id"] + " in file " + filename )
            if rule["id"] == "GitHub access token":
                token = line[match.regs[0][0]:match.regs[0][1]]
                print("This is it: " + token)
                h = Github(token)
                user = h.get_user( )
                try:
                    print("This token is valid and belongs to " + user.login + "\n\n")
                except:
                    print("Mate, this token does not appear to be valid!\n\n")


def scan_diff( diff, rules ):
    diff = diff.splitlines()
    filename = "undef"
    for line in diff:
        if line[0:4] == '+++ ':
            filename = line[4:]
            print("File: " + filename)
        elif line[0] == '+':
            scan_line( filename, line[1:], rules )


def process_repo( token, repo ):
    # login to github with our token
    g = Github(token)

    if repo == None:
        # We're going to grab the first repo for this user.
        print("No repo provided, so I'll choose a repo from this user")
        repo = g.get_user().get_repos()[0]
    else:
        repo = g.get_repo(repo)

    print (repo)

    rules = read_rules("rules.json")
    print("Rules loaded.")

    for commit in repo.get_commits( ):
        # print(commit)
        diff_url = commit.html_url+".diff"
        print(diff_url)
        r = requests.get( diff_url )
        scan_diff( r.text, rules )
        print("----------------------------------------")


def test_github_access_token( ):
    line = "token = ghp_donkeyChickenMouseNoodleCowPigZebras;"  # fake token, can our scanner verify that?
    filename = "test.c"
    rules = read_rules("rules.json")
    scan_line( filename, line, rules )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 " + sys.argv[0] + " [repo_url]")
        sys.exit()
    else:
        repo = sys.argv[1]
        if repo[0:19] == "https://github.com/":
            repo = repo[19:]
        if repo[0:18] == "http://github.com/":
            repo = repo[18:]
        print(repo)

    if 'token' in os.environ:
        token = os.environ['token']
    else:
        print("I require an access token to work")
        print("try: export token=...")
        sys.exit()

    process_repo(token, repo)


