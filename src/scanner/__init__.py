import re

from rules.rules import rules

# def scan_chunk( filename, chunk, rules ):
def scan_chunk( filename, chunk ):
    results = []
    # for rule in rules["rules"]:
    for rule in rules:
        match = re.findall(rule["regex"], chunk)
        if match:
            for secret in match:
                result = { "id": rule["id"], "rule": rule["name"], "file": filename, "secret": secret, "confirmed": False }
                print("*************************************************************")
                print(f"Found [{rule['id']}] {rule['name']} in file {filename}")
                print(secret)

                if "validate" in rule:
                    result["confirmed"] = rule["validate"](secret)
                else:
                    result["confirmed"] = "N/A"

                results.append(result)
    return results

# def scan_diff( diff, rules ):
def scan_diff( diff ): 
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
            # results = scan_chunk( filename, chunk, rules )
            results = scan_chunk( filename, chunk )
            all_results = all_results + results
            chunk = ""
    return all_results
