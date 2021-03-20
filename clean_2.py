import re


def solution(program, flag_rules, commands):
    def check_args_type(flag):
        '''
        Returns True flag argument is valid or False

        if rules are added, you can add them here

        input:
            flag(string) = "<flag_name> <flag argument>"
            ex) "f file"
        '''

        tokens = flag.strip().split()
        flag_name = tokens[0]
        if len(tokens) < 1: # more than two flag_arguments or no flag_arguments
            return False
        if re.search(flag_pattern, flag_name) is None: # flag pattern checked
            return False
        if flag_name not in rules.keys(): # invalid flag
            return False
        if rules[flag_name] != "NULL" and len(tokens) == 1: # no argument needed
            return False
        if rules[flag_name] == "NULL" and len(tokens) > 1:  # no argument needed
            return False
        if not rules[flag_name].endswith("S") and len(tokens) > 2: # number of arugument checked
            return False
        if rules[flag_name].startswith("STRING"):
            str_chk = any([re.search("[a-zA-Z]", t) is None for t in tokens[1:]]) #argument type str checked
            if str_chk:
                return False
        if rules[flag_name].startswith("NUMBER"):
            num_chk = any([re.search("[0-9]", t) is None for t in tokens[1:]]) # argument type number checked
            if num_chk:
                return False
        return True

    # Rule Processing
    answer = []
    flag_pattern = re.compile("[a-zA-Z]{1,9}")
    rules = {} # rules = {"s": "STRING", }
    for rule in flag_rules:
        flag, arg_type = rule.split()
        rules[flag[1:]] = arg_type

    # Checking validity of commands
    for command in commands:
        ans = True
        # check if program name is valid or not
        if command.split("-")[0].strip() != program:
            ans = False
            answer.append(ans)
            continue

        # leave flags only
        flags = command.split("-")[1:]

        for flag in flags: # flag: "s xxx" or "f"
            if check_args_type(flag) is False:
                ans = False
                break

        answer.append(ans)

    return answer

