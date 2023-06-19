
# 그래프 생성
import collections
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    # 각 요소가 갈 수 있는 목적지
}
# 맵을 저장하기 위한 자료형 생성
visited = set()
# 너비 우선 탐색
def bfs_iterative(start_node):
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
# 깊이 우선 탐색
def dfs_iterative(start_node):
    stack = [start_node] # 방문할 위치 쌓기

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            stack.extend(reversed(graph[node]))



snode = 'A'
dfs_iterative(snode)
visited.clear()
print('\n-----')
bfs_iterative(snode)