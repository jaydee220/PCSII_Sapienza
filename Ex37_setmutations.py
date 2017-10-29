if __name__ == "__main__":
    input()
    set1 = set(input().split())
    for _ in range(int(input())):
        getattr(set1, input().split()[0])(input().split())
    print(sum(map(int, set1)))