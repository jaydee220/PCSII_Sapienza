from itertools import groupby
if __name__ == "__main__":
    outputlst = [(len(list(count)), int(item)) for item, count in groupby(input())]
    print(*outputlst)
