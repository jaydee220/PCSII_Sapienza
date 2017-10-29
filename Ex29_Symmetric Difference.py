if __name__ == "__main__":
    outputlst = [set(input().split()) for _ in range(4)]
    l1 = list(map(int, outputlst[1].difference(outputlst[3])))
    l2 = list(map(int, outputlst[3].difference(outputlst[1])))
    output = sorted(l1+l2)
    output = list(map(str, output))
    print ("\n".join(output))