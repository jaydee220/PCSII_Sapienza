def is_leap(year):
    leap = True
    if (year >= 1900) and (year <= 10**5):
        if (year%4 != 0):
            leap=False
        elif (year%100 !=0):
            leap=True
        elif (year%400 !=0):
            leap=False
    return leap