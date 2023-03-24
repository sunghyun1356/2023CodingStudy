n = int(input())

first = list(map(int, input().rstrip('\n')))
second = list(map(int, input().rstrip('\n')))


def change(num):
    if num==0:
        return 1
    else:
        return 0
def switch(array, cnt):
    if cnt ==1:
        array[0] = change(array[0])
        array[1] = change(array[1])
    for i in range(1,n):
        if array[i-1] != second[i-1]:
            cnt+=1
            array[i-1] = change(array[i-1])
            array[i] = change(array[i])
            if i !=n-1:
                array[i+1] = change(array[i+1])
    if array == second:
        return cnt
    else:
        return -1
yes = switch(first[:], 0)
no = switch(first[:], 1)
if yes >=0 and no >=0:
    print(min(yes, no))
elif yes >=0 and no <0:
    print(yes)
elif yes <0 and n0 >=0 :
    print(no)
else:
    print(-1)
        
       
    