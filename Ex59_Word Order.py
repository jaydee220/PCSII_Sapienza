from collections import Counter, OrderedDict
#class from python documentation for ordered counters
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

if __name__ == "__main__":
    elements = OrderedCounter(input() for _ in range(int(input())))
    print (len(elements))
    [print (y,end= " ") for x,y in [*list(elements.items())]]