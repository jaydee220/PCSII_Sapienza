from collections import Counter
if __name__ == "__main__":
    totshoes = int(input())
    stock = Counter(map(int, input().split()))
    sales = int(input())
    output_price = 0
    for _ in range(sales):
        size,price = map(int, input().split())
        if stock[size]:
            output_price += price
            stock[size] -= 1
    print (output_price)