from collections import OrderedDict
def merge_the_tools(string, k):
    outputset=[]
    outputlst1 = []
    generator = [(string[x:x + k] for x in range(0, len(string), k))]
    for s in generator:
        outputlst = list(s)
    outputlst = [OrderedDict.fromkeys(x).keys() for x in outputlst]
    for outputln in outputlst:
        print(*outputln, sep="",end="\n")




if __name__ == "__main__":
    merge_the_tools("AABCAAADA",3)