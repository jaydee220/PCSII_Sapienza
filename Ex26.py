def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    stuart = 0
    kevin = 0
    check = []
    for let in range(len(string)):
            subs = string[let]
            if string[let] in vowels:
                i = len(string)
                while let != i:
                   kevin +=1
                   i -= 1
            else:
                i = len(string)
                while let != i:
                    stuart += 1
                    i -= 1

    if stuart > kevin:
        print("Stuart "+str(stuart))
    elif stuart < kevin:
        print("Kevin "+str(kevin))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
