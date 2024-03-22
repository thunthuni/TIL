# 그래프:
: 아이템들과 이다르 사이의 연결 관계를 표현한다

- 선형 자료구조나 트리 자료구조로 표현하기 어려운 N:N관계를 가지는 원소들을 표현하기에 용이하다

## 종류
- 무향 그래프 (undirected graph)
  - : 양방향 
- 유향 그래프 (directed graph)
  - : 단방향
- 가중치 그래프 (weighted graph)
- 완전 그래프
  - : 정점들에 대해 가능한 모든 간선들을 가진 그래프
- 부분 그래프
  - : 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프 

## 용어 정리
- 인접
  - 두 개의 정점에 간선이 존재하면서 서로 인접
- 그래프 경로
  - 간선들을 순서대로 나열
  - 단순경로: 경로 중 한 정점을 최대한 한번만 지나는 경로
  - 사이클: 시작한 정점에서 끝나는 경로 
    - 1-3-5-1

## 코코드드
- 인접 행렬
- 인접 리스트 

### 인접 행렬 
- V*V 배열을 활용해서 표현
- 갈 수 없다면 0, 있다면 1을 저장
- 장점: 
  - 노드간의 연결 정보를 한 방에 확인 가능 
  - 행렬곱을 이용해서 탐색이 쉽게 가능
  - 간선이 많을수록 glass
- 단점:
  - 노드 수가 커지면 메모리가 낭비
    - 연결이 안된 것도 저장
    - **노드 수와 메모리 제한 반드시 확인할 것**

### 인접 리스트
- V개의 노드가 갈 수 있는 정보만 저장
- 장점:
  - 메모리 사용량이 적다 
  - 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율적

```python

visited = [0]*5

def dfs(now):
  # 기저 조건

  # 다음 재귀 호출 전
  visited[now] = 1
  print(now, end='')
  
  # 다음 재귀 호출
  # dfs: 현재 노드에서 다른 노드들을 확인
  # 다른 노드들 == 반복문
  for to in range(5):
    # 갈 수 없다면 pass
    if graph[now][to] == 0:
      continue

    dfs(to)

  # 돌아왔을 때 작업
```
```python
visited = [0]*5

def dfs(now):
  # 기저 조건

  # 다음 재귀 호출 전
  visited[now] = 1
  print(now, end='')
  
  # 다음 재귀 호출
  # 인접 리스트
  # 1. 갈 수 없는 곳 조건 필요없음
  # 2, for 문 작성 수정
  for to in graph[now]:
    # 이미 방문했다면 pass
    if visited[to]:
      continue

    visited[to] = 1
    path.append(to)
    dfs(to)

  # 돌아왔을 때 작업
```
```python 
visitied = [0] * 5
def bfs(start):

  # 시작 노드를 큐에 추가 + 방문 표시 
  queue = [start]
  visited[start] = 1

  while queue: 
    now = queue.pop(0)
    print(now, end=' ')

    # 갈 수 있는 곳을 체크
    for to in range(5):
      if graph[now][to] == 0:
        continue
      
      if visited[to]:
        continue
      
      visited[to] = 1
      # print(visited)
      queue.append(to)

```
- 딕셔너리로 
```python
visited = [0] * 5
def bfs(start):
  queue = [start]
  visited[start] = 1

  while queue:
    now = queue.pop(0):
    print(now, end= ' ')

    for to in graph[now]:
      if visited[to]:
        continue
      
      visited[to] = 1
      print(visited)
      queue.append(to)

bfs(0)

    # 갈 수 있는 곳을 체크 

```

# 서로소 집합
: 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들이다.
  - 교집합이 없다 

- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분: Representative

- 표현 방법:
  - 연결 리스트
  - 트리 
- 상호배타 집합 연산
  - Make-set(x)
    - 집합 만들기
    - 처음엔 자기자신이 대표 
  - Find-set(x)
  - Union(x, y)
  
```python 
# 1~6 번까지 노드가 존재
# 1. make_set
def make_set(n):
  return [i for i in range(n)]

# 1~6번까지를 사용하기 위해 7개 생성
parents = make_set(7)

# 2. find_set: 대표자를 찾아보자
  # 부모 노드를 보고, 부모 노드도 연결이 되어 있다면 다시 반복
  # until 자기 자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
  # 자기 자신이 대표 -> 끝
  if parents[x] == x:  
    return x
  
  # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다.
  return find_set(parents[x])

# 3. union
def union(x, y):
  x = find_set(x)
  y = find_set(y)
  # 이미 같은 집합에 속해있다면 continue
  if x == y :
    return 
  # 다른 집합이라면 합침
  # ex) 더 작은 루트노트에 합쳐라
  if x < y:
    parents[y] = x
  else:
    parents[x] = y
  
  union(1,3)
  union(2,3)
  union()

  

```