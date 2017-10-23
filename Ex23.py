def print_formatted(number):
    # your code goes here
    space = len(format(number,"b"))+1
    output_lst = []
    for i in range(1,number+1):
        line = []
        line += format(i,"d").rjust(space-1," ")
        line += format(i,"o").rjust(space," ")
        line += format(i,"x").upper().rjust(space," ")
        line += format(i,"b").rjust(space," ")
        output_lst.append("".join(line))
    return print ("\n".join(output_lst))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)