if __name__ == "__main__":
    a = input()
    set_eng = set(input().split())
    b = input()
    set_fr = set(input().split())
    print (len(set_eng.intersection(set_fr)))
