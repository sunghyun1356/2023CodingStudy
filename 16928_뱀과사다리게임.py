from collections import deque

ladder =[0]*101
snake =[0]*101
n, m = map(int, input().split())
for i in range(n):
    first, second = map(int, input().split())
    ladder[first] = second
for i in range(m):
    first, second = map(int, input().split())
    snake[first]=second    

check =[0] * 101
visited =[False] * 101


def BFS():
    q = deque([1])
    while q:
        now = q.popleft()
        if now ==100:
            print(check[now])
            break
        
        for dice in range(1,7):
            next = now + dice
            if next <= 100 and not visited[next]:
                if ladder[next] != 0:
                    next = ladder[next]
                if snake[next] != 0:
                    next = snake[next]
                if not visited[next]:
                    visited[next] = True
                    check[next] = check[now] +1
                    q.append(next)                    
BFS()
                
    