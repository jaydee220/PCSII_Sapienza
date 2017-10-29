if __name__ == "__main__":
    lens_set_lst = list(input().split())
    comp_lst = list(input().split())
    set_a = set(input().split())
    set_b = set(input().split())
    a = 0
    b = 0
    for val in comp_lst:
        if val in set_a:
            a += 1
        if val in set_b:
            b += 1
    print (a-b)
