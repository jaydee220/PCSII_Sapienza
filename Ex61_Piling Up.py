from collections import deque
if __name__ == "__main__":
    for _ in range(int(input())):
        _, horizontal = input(), deque(map(int, input().split()))
        print (sorted(horizontal))
        for vertical in sorted(horizontal):
            if horizontal[0] == vertical:
                horizontal.popleft()

        # for cube in reversed(sorted(queue)):
        #     if queue[-1] == cube:
        #         queue.pop()
        #     elif queue[0] == cube:
        #         queue.popleft()
        #     else:
        #         print('No')
        #         break
        # else:
        #     print('Yes')