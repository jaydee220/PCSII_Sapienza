if __name__ == "__main__":
    inputset = set(input().split())
    print (all(inputset > set(input().split()) for _ in range(int(input()))))