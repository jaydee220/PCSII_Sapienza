from collections import deque
if __name__ == "__main__":
    for _ in range(int(input())):
        _, horizontal = input(), deque(map(int, input().split()))
        for vertical in sorted(horizontal)[::-1]:
            if horizontal[-1] == vertical:
                horizontal.pop()
            elif horizontal[0] == vertical:
                horizontal.popleft()
            else:
                print ("No")
                break
        else:
            print("Yes")
