if __name__ == '__main__':
    Z = int(input())
    N = []
    for cmd in range(Z):
        N.append(input())
    output_lst = []
    for code_ln in range(len(N)):
        code_lst = N[code_ln].split(' ')
        if "print" in code_lst:
            command = "print(output_lst)"
        elif len(code_lst) == 3:
             command = "output_lst."+code_lst[0]+"("+code_lst[1]+","+code_lst[2]+")"
        elif (len(code_lst) == 2) and (code_lst[1]!= ""):
             command = "output_lst."+code_lst[0]+"("+code_lst[1]+")"
        else:
             command = "output_lst." + code_lst[0] + "("+")"
        exec(command)




