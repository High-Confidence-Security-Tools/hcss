import json

def read_rules( rulesfile="src/rules/rules.json" ):
    with open(rulesfile, 'r') as f:
        rules = json.loads( f.read() )
    # print( json.dumps(rules, indent=2) )
    return rules

# def test_github_access_token( ):
#     line = "token = ghp_donkeyChickenMouseNoodleCowPigZebras;"  # fake token, can our scanner verify that?
#     filename = "test.c"
#     rules = read_rules()
#     scan_line( filename, line, rules )
