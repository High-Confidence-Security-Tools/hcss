from github import Github


def rsa_private_key(secret):
    """ Validate HCSS-1 """
    # TODO replace with actual RSA key validation
    try:
        if 'RSA' in secret:
            return True
    except:
        return False

def github_access_token(secret):
    """ Validate HCSS-2 """
    try:
        h = Github(secret)
        user = h.get_user( )
        print("This token is valid and belongs to " + user.login + "\n\n")
        return True
    except: # TODO specific exception handling
        print("Mate, this token does not appear to be valid, so I will not record it!\n\n")
        return False
