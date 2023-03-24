import heapq
heap =[]
n= int(input())
for _ in range(n):
    value, day = map(int, input().split())
    heap.append([value, day])
    
heap = sorted(heap, key=lambda x : x[1])
sums = []
for num in heap:
    heapq.heappush(sums, num[0])
    if(len(sums)>num[1]):
        heapq.heappop(sums)
print(sum(sums))
    
