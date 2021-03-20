# 문제 1

if 0:
    def solutions(table, languages, preference):

        jg = {} # jg {"직군": {"언어": 점수,,,,,} }

        for line in table:
            li = line.split()
            jg[li[0]] = {}
            for i, l in enumerate(li[1:]):
                jg[li[0]][l] = 5 - i
        score = {}

        for jik in jg.keys():
            score[jik] = 0
            for ll, pre in zip(languages, preference):
                if ll in jg[jik].keys():
                    score[jik] += jg[jik][ll] * pre

        answer = sorted(score, key=lambda x: (-score[x], x))

        return answer[0]


    print(solutions(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
              ["JAVA", "JAVASCRIPT"], [7, 5]))


# 문제 2
if 0:

    def solution(inp_str):
        import re
        answer = []
        if len(inp_str) < 8 or len(inp_str) > 15:
            answer.append(1)

        patt = re.compile("[^A-Za-z0-9\~\!\@\#\$\%\^\&\*]")
        if re.search(patt, inp_str):
            print(re.search(pat, inp_str).group())
            answer.append(2)

        pat1 = re.compile("[A-Z]")
        pat2 = re.compile("[a-z]")
        pat3 = re.compile("[0-9]")
        pat4 = re.compile("[\~\!\@\#$\%\^\&\*]")

        check_3 = [re.search(pat1, inp_str) is not None,
                   re.search(pat2, inp_str) is not None,
                   re.search(pat3, inp_str) is not None,
                   re.search(pat4, inp_str) is not None]

        if sum(check_3) < 3:
            answer.append(3)

        last = "_"
        for i, ch in enumerate(inp_str):
            if i + 3 < len(inp_str):
                if ch * 4 == inp_str[i:i+4]:
                    answer.append(4)
                    break
            else:
                break

        cnt = {}
        for ch in inp_str:
            if ch in cnt.keys():
                cnt[ch] += 1
                if cnt[ch] >= 5:
                    answer.append(5)
                    return answer
            else:
                cnt[ch] = 1

        if len(answer) == 0:
            answer.append(0)

        return answer

    print(solution("asdbaewrnaertnaerAA1D@"))

# 문제 3
if 0:
    def solution(enter, leave):
        cnt = [0] * (len(enter) + 1)

        for l in leave:
            ind = enter.index(l)
            room = sum([a != -1 for a in enter[:ind]])
            for i in range(ind + 1):
                if enter[i] != -1:
                    cnt[enter[i]] += room
            enter[ind] = -1

        return cnt[1:]

    print(solution([3, 2,1], [2, 1, 3]))

# 문제 4 실패요 ,,,, 마지막에 급하게 마구마구 짜다가 ... 망한 코드
if 0:
    def solution(data, word):
        import re

        tree = [[0] for _ in range(len(data) + 10)]
        graph = {}
        parent_tree = [[0] for _ in range(len(data) + 10)]
        dolls = {}
        isdoll = [0] * (len(data) + 10)
        isdesc = [0] * (len(data) + 10)
        for d in data:
            index, name, parent = d.split()
            graph[index] = name
            tree[int(parent)].append({"index": int(index), "name": name})
            parent_tree[int(index)].append(int(parent))

        print(tree)
        for idx, tt in enumerate(tree):
            if len(tt) == 1:
                isdoll[idx] = 1
                if graph[str(idx)] not in dolls.keys():
                    dolls.append({"name": [graph[str(idx)]] , "index": idx})
            else:
                isdesc[idx] = 1

        li = []

        def print_answer(ind):
            if ind == 0:
                return
            li.append(graph[str(ind)])
            for p in parent_tree[ind]:
                print_answer(p)

        if word in dolls.keys():
            print_answer(dolls[word])

        return "/".join(li[::-1])

    print(solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"], "BROWN"))










