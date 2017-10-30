from collections import defaultdict
if __name__ == "__main__":
    na,mb = map(int,input().split())
    a = defaultdict(list)
    for indicesa in range(1,na+1):
        a[input()].append(str(indicesa))
    for indicesb in range(mb):
        print (' '.join(a[input()]) or -1)