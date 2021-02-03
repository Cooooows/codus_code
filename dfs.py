# DFS 정의
# 깊이 우선 탐색
# graph : 주어진 그래프
# V : 현재 노드
# visited : 방문 여부 (boolean)
def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 노드 방문(재귀)
    for i in graph[v]:              # 현재 노드와 연결된 노드들
        if not visited[i]:          # 선택된 노드에 아직 방문 안했을 떄
            dfs(graph, i, visited)  # dfs 수행


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

# 노드의 방문 여부 나타내는 리스트
visited = [False] * 9

dfs(graph,4,visited)