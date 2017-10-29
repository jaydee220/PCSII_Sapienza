from itertools import permutations
if __name__ == "__main__":
    inputlst = input().split()
    output = list(permutations(inputlst[0],int(inputlst[1])))
    output.sort()
    for i in output:
        print ("".join(i))