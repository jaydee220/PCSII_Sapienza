from collections import Counter
if __name__ == "__main__":
    nmbr =  int(input())
    inlist = input().split()
    inset = set(inlist)
    counter= Counter(inlist)
    print (counter.most_common()[:-2:-1][0][0])
