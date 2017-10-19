if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    high_nr = max(arr)
    while high_nr == max(arr):
        arr.remove(high_nr)
    print(max(arr))

