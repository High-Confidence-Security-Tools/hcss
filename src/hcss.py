import os
import json
import re
import sys

from argparse import ArgumentParser

from providers import parse_provider


def parse_args():
    parser = ArgumentParser(description='Search for secrets with high confidence')
    parser.add_argument('repo_url', help='URL of a git repository')

    return parser.parse_args()

def output_results( results ):
    if results == []:
        print("\nMate, I tried the best I could, but couldn't find any secrets :-(\n")
    else:
        print("\n*** Here are the findings: ***\n")
        for result in results:
            print( json.dumps(result, indent = 2) )
            print( "----------------------------------------" )

if __name__ == "__main__":
    args = parse_args()

    repo_url = args.repo_url
    process_repo, url_path = parse_provider(repo_url)

    if 'token' in os.environ:
        token = os.environ['token']
    else:
        print("I require an access token to work")
        print("try: export token=...")
        sys.exit()

    results = process_repo(token, url_path)
    output_results(results)
