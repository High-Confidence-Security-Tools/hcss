import json
import os
import logging

from providers import github

from flask import Flask, request, jsonify
from providers import bitbucket

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

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
        logging.info("Mate, I tried the best I could, but couldn't find any secrets :-(")
    else:
        logging.info("*** Here are the findings: ***")
        for result in results:
            logging.info( json.dumps(result, indent = 2) )
            logging.info( "----------------------------------------" )

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
            results = github.process_single_commit( github_token, commit_url )
            all_results = all_results + results
        if all_results != []:
            logging.info("--------- inline comment happening on results ----")
            for result in all_results:
                # leave inline comments
                commit_url = result["commit_url"]
                path = result["file"][2:]   # the diff starts out with "b/", so remove that part
                position = result["position"]
                comment = "Good Lord, do you realise what you have done?!  Please do not commit secrets to source code repositories!  You better revoke this right now, as I promise you that people seeing this are in the process of hacking it!"
                github.leave_comment_on_commit( github_token, commit_url, path, position, comment)
        output_results(all_results)
        return jsonify({'success':True}), 200
    else:
        return jsonify({'message':'No Content'}), 204

@app.route("/bitbucket_push", methods=['POST'])
def bitbucket_post_webhook():
    content = request.get_json()
    if content is None:
        return jsonify({'message':'No Content'}), 204
    else:
        all_results = bitbucket.process_repo(content, leave_comments=True)
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
            results = github.process_single_commit( github_token, commit_url )
            all_results = all_results + results
        output_results(all_results)
        return jsonify({'success':True}), 200
    else:
        return jsonify({'message':'No Content'}), 204

#if __name__ == '__main__':
