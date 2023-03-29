import sys
read = lambda : sys.stdin.readline().rstrip()

n, m = map(int, read().split())

a = list(map(int, read().split()))
b = list(map(int, read().split()))

answer = a+b

answer.sort()
print(*answer)






    