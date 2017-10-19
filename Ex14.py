def swap_case(s):
    output_lst = []
    for letter in s:
       if isinstance(letter,str):
           output_lst.append(letter.swapcase())
       else:
           output_lst.append(letter)
    return ''.join(output_lst)

if __name__ == '__main__':
    print (swap_case("test123.Com"))