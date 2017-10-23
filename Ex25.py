def capitalize(strng):
    for wrd in strng.split():
        strng = strng.replace(wrd,wrd.capitalize())
    return strng