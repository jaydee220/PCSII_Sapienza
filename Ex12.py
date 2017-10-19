classgrades= []
if __name__ == '__main__':
    for _ in range(int(input())):
        names = input()
        scores = float(input())
        classgrades.append([names,scores])
    gradesonly = list(set(scores for names,scores in classgrades))
    gradesonly.sort()
    names_lst = list(names for names,scores in classgrades if scores == gradesonly[1])
    names_lst.sort()
    for name in names_lst:
        print (name)
