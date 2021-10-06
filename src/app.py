from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def heartbeat():
    return "<p>I am alive!</p>"


@app.route("/github_push", methods=['POST'])
def github_post_webhook():
    print (request.is_json)
    content = request.get_json()
    print(json.dumps( content, indent = 2))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


