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

        if len(tokens) > 2 or len(tokens) < 1:  # more than two flag_arguments or no flag_arguments
            return False

        flag_name = tokens[0]
        if re.search(flag_pattern, flag_name) is None:  # flag pattern checked
            return False
        if flag_name not in rules.keys():  # invalid flag
            return False
        if rules[flag_name] != "NULL" and len(tokens) == 1:  # argument needed
            return False
        if rules[flag_name] == "NULL" and len(tokens) > 1:  # no argument allowed
            return False
        if rules[flag_name] == "STRING" and re.search("[^a-zA-Z]", tokens[1]):  # argument type string checked
            return False
        if rules[flag_name] == "NUMBER" and re.search("[^0-9]", tokens[1]):  # argument type number checked
            return False

        return True

    # Rule Processing
    answer = []
    flag_pattern = re.compile("[a-zA-Z]{1,9}")
    rules = {}  # rules = {"s": "STRING", }
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

        for flag in flags:  # flag: "s xxx" or "f"
            if check_args_type(flag) is False:
                ans = False
                break

        answer.append(ans)

    return answer
