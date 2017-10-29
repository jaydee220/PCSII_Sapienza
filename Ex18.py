def count_substring(string, sub_string):
    output = 0
    for letter_id in range(len(string)):
        word_index=letter_id+len(sub_string)
        if string[letter_id:word_index] == sub_string:
            output +=1
    return output

