if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[c1,c2,c3] for c1 in range(x+1) for c2 in range(y+1) for c3 in range(z+1) if ((c1+c2+c3) != n)])