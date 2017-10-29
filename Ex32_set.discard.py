if __name__ == '__main__':
    set_len = int(input())
    inp_set = set(map(int,input().split()))
    com_len = int(input())
    com_lst = []
    for _ in range(com_len):
        com_lst.append(input())
    for code_ln in range(com_len):
        code_lst = com_lst[code_ln].split(' ')
        if (len(code_lst) == 2) and (code_lst[1]!= ""):
             command = "inp_set."+code_lst[0]+"("+code_lst[1]+")"
        else:
             command = "inp_set." + code_lst[0] + "("+")"
        exec(command)
    print (sum(inp_set))