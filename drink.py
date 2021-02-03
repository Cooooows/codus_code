import time
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

start = time.time()  # 시작 시간 저장


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 방문하지 않았을 때
    if graph[x][y] == 0:
        # 방문하고
        graph[x][y] = 1
        # 연결된 부분 판단
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    # 이미 방문했으면 False
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
print("time :", time.time() - start)