classgrades= []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        scores = float(input())
        classgrades.append([name,scores])
    gradesonly = list(set(scores for name,scores in classgrades))
    gradesonly.sort()
    names

