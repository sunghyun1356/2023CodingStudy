n = int(input())
first = list(map(int,input().split()))
m = int(input())
second = list(map(int,input().split()))
first.sort()
def bi_search(array, target, start, end):
    while start <= end:
        mid = (start +end)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] >target:
            end = mid -1
        else:
            start = mid +1
    return None

for i in range(m):
    if bi_search(first, second[i], 0, n-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
        
