import re


def solution(program, flag_rules, commands):
    def check_args_type(flag):
        '''
        Returns True flag argument is valid or False

        *** if rules are added, you can add them here ***

        input:
            flag(string) = "<flag_name> <flag argument>"
            ex) "f file"
        '''

        tokens = flag.strip().split()

        if len(tokens) < 1:  # more than two flag_arguments or no flag_arguments
            return False

        flag_name = tokens[0]
        if flag_name not in rules.keys() and flag_name in alias.keys():  # alias to flag
            flag_name = alias[flag_name]
        if re.search(flag_pattern,flag_name) is None:  # flag pattern checked
            return False
        if flag_name not in rules.keys() or chk_duplicate_rules[flag_name] is False:  # invalid flag (does not exist or is already used)
            return False
        if rules[flag_name] != "NULL" and len(tokens) == 1:  # no argument needed
            return False
        if rules[flag_name] == "NULL" and len(tokens) > 1:  # no argument needed
            return False
        if not rules[flag_name].endswith("S") and len(tokens) > 2:  # number of arugument checked
            return False
        if rules[flag_name].startswith("STRING"):
            str_chk = any([re.search("[a-zA-Z]", t) is None for t in tokens[1:]])  # argument type str checked
            if str_chk:
                return False
        if rules[flag_name].startswith("NUMBER"):
            num_chk = any([re.search("[0-9]", t) is None for t in tokens[1:]])  # argument type number checked
            if num_chk:
                return False

        chk_duplicate_rules[flag_name] = False
        return True

    # Rule Processing
    answer = []

    flag_pattern = re.compile("[a-zA-Z]{1,9}")

    rules = {}  # rules = {"s": "STRING", }
    alias = {}  # alias = {"amount": "a", }
    chk_duplicate_rules = {}

    for rule in flag_rules:
        li = rule.split()
        if len(li) == 2:
            flag, arg_type = li
            rules[flag[1:]] = arg_type
            chk_duplicate_rules[flag[1:]] = True
        else:
            al, _, flag = li
            alias[al[1:]] = flag[1:]

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

        for flag in flags:  # flag: "s xxx" or "f"
            if check_args_type(flag) is False:
                ans = False
                break

        answer.append(ans)

    return answer
