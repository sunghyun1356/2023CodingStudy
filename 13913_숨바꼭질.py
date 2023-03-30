from collections import deque



def check(i):
    if i <0 or i > row-1:
        return True
    return False

def path(now):
    arr=[]
    temp = now
    for _ in range(cost[now]+1):
        arr.append(temp)
        temp = checked[temp]
    print(' '.join(map(str, arr[::-1])))


def BFS():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now ==k:
            print(cost[now])
            path(now)
            return
        for i in (now -1, now +1, now*2):
            if check(i):
                continue
            if cost[i] ==0:
                q.append(i)
                cost[i] = cost[now] +1
                checked[i] = now
        


n, k = map(int, input().split())

checked = [0] * 100001

cost = [0] * 100001

row = 100001

BFS()
