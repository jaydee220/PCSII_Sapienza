from itertools import combinations
if __name__ == "__main__":
    inputlst = input().split()
    inputwrd = list(inputlst[0])
    inputwrd.sort()
    for i in range (1,int(inputlst[1])+1):
        output = list(combinations(inputwrd,i))
        output.sort()
        for i in output:
            print ("".join(i))