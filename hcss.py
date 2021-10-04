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


def scan_chunk( filename, chunk, rules ):
    results = []
    for rule in rules["rules"]:
        match = re.findall(rule["regex"], chunk)
        if match:
            for secret in match:
                result = { "rule": rule["id"], "file": filename, "secret": secret, "confirmed": False }
                print("*************************************************************")
                print("Found " + rule["id"] + " in file " + filename )
                print(secret)
                if rule["id"] == "GitHub access token":
                    h = Github(secret)
                    user = h.get_user( )
                    try:
                        print("This token is valid and belongs to " + user.login + "\n\n")
                        result["confirmed"]=True
                    except:
                        print("Mate, this token does not appear to be valid, so I will not record it!\n\n")
                        continue
                results.append(result)
    return results


def scan_diff( diff, rules ):
    all_results = []
    diff = diff.splitlines()
    filename = "undef"
    chunk = ""
    for line in diff:
        if line[0:4] == '+++ ':         # file where lines are added
            filename = line[4:]
            chunk = ""
            print("File: " + filename)
        elif line[0:4] == '--- ':       # previous file
            continue
        elif line[0:2] == "@@":         # line numbers before and after
            continue
        elif line[0:1] == '+':
            chunk = chunk + line[1:] + "\n"
        elif chunk != "":
            results = scan_chunk( filename, chunk, rules )
            all_results = all_results + results
            chunk = ""
    return all_results


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

    all_results = []
    for commit in repo.get_commits( ):
        # print(commit)
        diff_url = commit.html_url+".diff"
        print(diff_url)
        r = requests.get( diff_url )
        diff_text = r.text
        if len(diff_text) < 1048576:
            results = scan_diff( r.text, rules )
            # TODO: insert commit URL into each result
            for result in results:
                result["commit_url"] = commit.html_url
            all_results = all_results + results
        else:
            print("Diff is huge, will skip this one")
        print("----------------------------------------")
    return all_results


def test_github_access_token( ):
    line = "token = ghp_donkeyChickenMouseNoodleCowPigZebras;"  # fake token, can our scanner verify that?
    filename = "test.c"
    rules = read_rules("rules.json")
    scan_line( filename, line, rules )


def output_results( results ):
    if results == []:
        print("\nMate, I tried the best I could, but couldn't find any secrets :-(\n")
    else:
        print("\n*** Here are the findings: ***\n")
        for result in results:
            print( json.dumps(result, indent = 2) )
            print( "----------------------------------------" )


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
        if repo[-1] == '/':
            repo = repo[0:-1]       # no trailing slash allowed
        print(repo)

    if 'token' in os.environ:
        token = os.environ['token']
    else:
        print("I require an access token to work")
        print("try: export token=...")
        sys.exit()

    results = process_repo(token, repo)
    output_results(results)


