def split_and_join(line):
    output_lst = line.split(" ")
    return "-".join(output_lst)

if __name__ == '__main__':
    print(split_and_join("as it is"))