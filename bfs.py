# BFS 정의
# 너비 우선 탐색

from collections import deque
def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:          # 뽑은 노드와 연결된 노드들
            if not visited[i]:      # 방문 안 한 노드일 경우
                queue.append(i)     # 큐에 넣고
                visited[i] = True   # 방문

# 2차원 리스트
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드 방문정보
visited = [False] * 9

bfs(graph,3,visited)