from itertools import combinations_with_replacement
if __name__ == "__main__":
    inputlst = input().split()
    inputwrd = list(inputlst[0])
    inputwrd.sort()
    output = list(combinations_with_replacement(inputwrd,int(inputlst[1])))
    output.sort()
    for i in output:
        print ("".join(i))