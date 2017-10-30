from collections import deque
if __name__ == "__main__":
    d = deque()
    nmb = int(input())
    com_lst = []
    for _ in range(nmb):
        com_lst.append(input())
    for code_ln in range(nmb):
        code_lst = com_lst[code_ln].split(' ')
        if (len(code_lst) == 2) and (code_lst[1]!= ""):
             command = "d."+code_lst[0]+"("+code_lst[1]+")"
        else:
             command = "d." + code_lst[0] + "("+")"
        exec(command)
    print(*d)