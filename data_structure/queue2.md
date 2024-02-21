# BFS
: 탐색 시작점의 **인접한 정점**들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

![Alt text](image-4.png)

```python
# V E : V 1~V번까지 V개의 정점. E개의 간선
# E개의 간선정보
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
def bfs(s, N):  #시작정점 s, 노드개수 N
    q = []  # 큐
    visited = [0] * (N+1)   # visited 
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문표시
    while q:   # 큐가 비워질때까지(남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할일
        print(t)
        for i in adjl[t]:  # t에 인접인 정점
            if visited[i] == 0:  # 방문하지 않은 정점이면 
                q.append(i)   # 인큐
                visited[i] = 1 + visited[t] # 방문표시
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i+2], arr[i*2+1]
# for i in range(0, E*2, 2)
#     n1, n2 = arr[i+2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 무향그래프 

bfs(1, v)
```
```python
def bfs(s, N):
    q = []
    visited = [0] * (N+1)
    q.append(s) # 시작점 인큐
    visited[s] = 1 #
    while q: 
        t = q.pop(0)  # 처리할 정점 디큐 
        if t == G:
            return visited[t] -1 # 최단 경로 간선 수
        for i in adjl[t]:   # t의 인접 정점이
            if visited[i]==0:      # 인큐되지 않았으면(처리된적이 없으면 )
                q.append(i)
                visited[i] = visited[t] +1
    return 0  # G까지 경로가 없는 경우 
    
V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i+2], arr[i*2+1]
# for i in range(0, E*2, 2)
#     n1, n2 = arr[i+2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 무향그래프 
```