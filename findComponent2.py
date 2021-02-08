import time
n = int(input())
data = list(map(int, input().split()))
m = int(input())
customer = list(map(int,input().split()))

stime = time.time()
data.sort()
start = 0
end = n-1
for i in customer:
    start = 0
    end = n - 1
    while True:
        mid = (start + end) // 2
        if start > end:
            print('no', end=' ')
            break
        if data[mid] == i:
            print('yes', end=' ')
            break
        elif data[mid] > i:
            end = mid - 1
        else:
            start = mid + 1


print("\ntime:" + str(time.time() - stime))