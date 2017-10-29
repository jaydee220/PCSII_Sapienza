if __name__ == "__main__":
    nmbr = int(input())
    country_set = set()
    for _ in range(nmbr):
        country_set.add(input())
    print (len(country_set))
