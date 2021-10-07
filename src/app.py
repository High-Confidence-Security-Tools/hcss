from flask import Flask, request, jsonify
import json
import os
from providers import github
from providers import bitbucket

required_vars = [
    'GITHUB_TOKEN',
    'BITBUCKET_USERNAME',
    'BITBUCKET_PASSWORD'
]
for var in required_vars:
    if var not in os.environ:
        raise SystemExit(f'ERROR: Required env variable not set ({var})')
    else: # TODO Move github authentication stuff to github provider module
        github_token = os.environ['GITHUB_TOKEN']

def output_results( results ):
    if results == []:
        print("\nMate, I tried the best I could, but couldn't find any secrets :-(\n")
    else:
        print("\n*** Here are the findings: ***\n")
        for result in results:
            print( json.dumps(result, indent = 2) )
            print( "----------------------------------------" )


app = Flask(__name__)

@app.route("/")
def heartbeat():
    return "<p>I am alive!</p>"


@app.route("/github_push", methods=['POST'])
def github_post_webhook():
    # TODO: verify signature
    content = request.get_json()
    if content is None:
        return jsonify({'message':'No Content'}), 204
    
    if 'commits' in content:
        all_results = []
        for commit in content["commits"]:
            commit_url = commit["url"]
            print(commit_url)
            results = github.process_single_commit( github_token, commit_url )
            all_results = all_results + results
        output_results(all_results)
        # print(json.dumps( content["commits"], indent = 2))
        return jsonify({'success':True}), 200
    else:
        return jsonify({'message':'No Content'}), 204

@app.route("/bitbucket_push", methods=['POST'])
def bitbucket_post_webhook():
    content = request.get_json()
    if content is None:
        return jsonify({'message':'No Content'}), 204
    else:
        all_results = bitbucket.process_repo(content)
        output_results(all_results)
        return jsonify({'success':True}), 200

### This is here to support deployment of the tool on a Google Cloud Function.
### Ignore for all other use cases
def github_post_webhook_gcp_cf(request):
    # TODO: verify signature
    content = request.get_json()
    if content is None:
        return jsonify({'message':'No Content'}), 204
    
    if 'commits' in content:

        all_results = []
        for commit in content["commits"]:
            commit_url = commit["url"]
            print(commit_url)
            results = github.process_single_commit( github_token, commit_url )
            all_results = all_results + results
        output_results(all_results)
        # print(json.dumps( content["commits"], indent = 2))
        return jsonify({'success':True}), 200
    else:
        return jsonify({'message':'No Content'}), 204

app.run()
