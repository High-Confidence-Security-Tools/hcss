import logging

from github import Github


logger = logging.getLogger(__name__)

def dummy_key(secret):
    """ 
    Validate HCSS-0

    This is a dummy key for testing so always returns true

    Parameters:
    secret (string): Secret to check

    Returns:
    bool: Whether it is valid or not
    """

    return True


def rsa_private_key(secret):
    """ 
    Validate HCSS-1

    Checks whether the discovered secret is a valid RSA key

    Parameters:
    secret (string): Secret to check

    Returns:
    bool: Whether it is valid or not
    """

    # TODO replace with actual RSA key validation
    try:
        if 'RSA' in secret:
            return True
    except:
        return False

def github_access_token(secret):
    """ 
    Validate HCSS-2 
    
    Checks whether the discovered secret is valid on Github.com

    Parameters:
    secret (string): Secret to check

    Returns:
    bool: Whether it is valid or not
    """

    try:
        h = Github(secret)
        user = h.get_user( )
        logging.info(f"This token is valid and belongs to {user.login}")
        return True
    except: # TODO specific exception handling
        logging.info("Mate, this token does not appear to be valid, so I will not record it!")
        return False
