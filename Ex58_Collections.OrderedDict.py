from collections import OrderedDict
if __name__ == "__main__":
    storage = OrderedDict()
    nmbr = int(input())
    for _ in range(nmbr):
        item, _, price = input().rpartition(" ")
        if not storage.__contains__(item):
            storage[item]=int(price)
        else:
            storage[item]+=int(price)
    for item, price in storage.items():
        print (item, price)