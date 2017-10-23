import string
def print_rangoli(size):
    letters = string.ascii_lowercase[:size]
    letters_flip = letters[::-1]
    output_lst = []
    for i in range(1,size+1):
        if i == 1:
             output_lst.append((letters[size-1]).center(size*4-3,"-"))
        else:
            output_lst.append(("-".join((letters_flip[0:i])+letters[-i+1:])).center(size*4-3,"-"))
    if size ==1:
        return print(letters[size-1])
    else:
        return print("\n".join(output_lst+output_lst[size-2::-1]))
