import cmath
if __name__ == '__main__':
    components = complex(input())
    print(abs(components))
    print(cmath.phase(components))