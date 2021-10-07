# Potential format for rules

from rules import validate

rules = [
    {
        "id": "HCSS-0",
        "name": "dummy key for testing",
        "regex": "dummy_key_for_testing[a-zA-Z0-9]*",
        "validate": validate.dummy_key
    },
    {
        "id": "HCSS-1",
        "name": "RSA private key",
        "regex": "-----BEGIN RSA PRIVATE KEY-----[0-9a-zA-Zi+\/=\\\"\\s]*-----END RSA PRIVATE KEY-----",
        "validate": validate.rsa_private_key
    },
    {
        "id": "HCSS-2",
        "name": "GitHub access token",
        "regex": "ghp_[0-9a-zA-Z]{35,40}",
        "validate": validate.github_access_token
    }
]
