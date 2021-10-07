# High Confidence Secret Scanner

This secret scanner aims to have no false positives.
Plus, there's more!  Stay tuned....

## Local Development
**Prerequisites:**
* Have Python 3.9 installed
* Have pipenv installed (`pip3 install pipenv`)

**Steps:**
* Set required environment variables:
```
export GITHUB_TOKEN=<personal access token>
export BITBUCKET_USERNAME=<username>
export BITBUCKET_PASSWORD=<app password>
```

* Setup virtualenv and install dependencies
```
pipenv install
```

* Shell into virtualenv
```
pipenv shell
```

* Start Flask server
```
python3 src/app.py
```
