from collections import deque
import time
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input())))

# 시작 시간
start = time.time()
result = 1
def bfs(x, y):
    global result
    queue = deque()
    queue.append((x, y))
    data[x][y] = result


    # 큐가 빌 때까지
    while queue:
        result = data[x][y]
        x, y = queue.popleft()


        for i in data:
            print(i)
        print()

        tx = x + 1
        ty = y
        if tx < n:
            if data[tx][ty] == 1:
                queue.append((tx, ty))
                data[tx][ty] = data[x][y] + 1
        tx = x
        ty = y + 1
        if ty < m:
            if data[tx][ty] == 1:
                queue.append((tx, ty))
                data[tx][ty] = data[x][y] + 1

        tx = x - 1
        ty = y
        if tx >= 0:
            if data[tx][ty] == 1:
                queue.append((tx, ty))
                data[tx][ty] = data[x][y] + 1

        tx = x
        ty = y - 1
        if ty >= 0:
            if data[tx][ty] == 1:
                queue.append((tx, ty))
                data[tx][ty] = data[x][y] + 1



    # # 큐가 빌 때까지
    # while queue:
    #     x, y = queue.popleft()
    #     # x = index / n
    #     # y = index % n
    #     # data[x][y] = 3
    #     result = result + 1
    #     print(result)
    #     print(x,y)
    #     tx = x + 1
    #     ty = y
    #     if tx < n:
    #         if data[tx][ty] == 1:
    #             queue.append((tx, ty))
    #     tx = x
    #     ty = y + 1
    #     if ty < m:
    #         if data[tx][ty] == 1:
    #             queue.append((tx, ty))
    #
    #     tx = x - 1
    #     ty = y
    #     if tx >= 0:
    #         if data[tx][ty] == 1:
    #             queue.append((tx, ty))
    #
    #     tx = x
    #     ty = y - 1
    #     if ty >= 0:
    #         if data[tx][ty] == 1:
    #             queue.append((tx, ty))

bfs(0, 0)
print(data[n-1][m-1])


