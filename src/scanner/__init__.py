import re

from rules.rules import rules


# how far into the chunk is the secret?  We need this so we can do automated inline comments
def offset_within_chunk( secret, chunk):
   
    index = chunk.index( secret )  # this is where are secret begins
    lines_up_to_secret = len( chunk[0:index].splitlines() )

    # secrets may be multi-lined.  We want to leave a comment at the end.  So find line number for that.
    # This is a little hairy.  We know where the secret begins, and we need to find how many lines
    # are in there until we get to the end.  Same approach as above...
    # Remark: this may seem excessively complicated, i.e. why not just search for the last line of the secret in the
    #   big chunk?  Answer:  because we need to make sure we are matching exactly the secret we are looking for.
    #   For example, if last_part_of_secret is '---- END RSA PRIVATE KEY ----', and there are more than one in the chunk,
    #   we don't want all our comments to fall under one of these cases.  Instead, we want once comment for each secret.
    secret_to_end_of_chunk = chunk[index:]  # secret starts here and goes all the way to the end of the whole chunk being processed
    last_part_of_secret = secret.splitlines()[-1]   # this is the last line of a possible multi-line secret
    index2 = secret_to_end_of_chunk.index( last_part_of_secret )    # we found the last line of the secret
    remaining_lines = len( secret_to_end_of_chunk[0:index2].splitlines() )
    
    return lines_up_to_secret - 1 + remaining_lines


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



def process_chunk( filename, chunk, line_number):
    lines_in_chunk = len( chunk.splitlines() )
    results = scan_chunk( filename, chunk )
    for result in results:
        offset = offset_within_chunk(result["secret"], chunk)
        line_number = line_number - lines_in_chunk + offset
        result["position"] = line_number
    return results

# def scan_diff( diff, rules ):
def scan_diff( diff ): 
    all_results = []
    diff = diff.splitlines()
    filename = "undef"
    chunk = ""
    line_number = 0   # need to keep track of line numbers 
    for line in diff:
        if line[0:4] == '+++ ':         # file with changes
            filename = line[4:]
            line_number = 0
            chunk = ""
            print("File: " + filename)
        elif line[0:4] == '--- ':       # the file before changes
            continue
        else:
            # these lines actually count for our automated inline commenting
            line_number = line_number + 1
            if line[0:1] == '+':
                chunk = chunk + line[1:] + "\n"
            else:
                # we're not adding new lines so we are at the end of a chunk
                if chunk != "":
                    results = process_chunk( filename, chunk, line_number)
                    all_results = all_results + results
                    chunk = ""
    return all_results
