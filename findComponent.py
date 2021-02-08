import time
n = int(input())
data = list(map(int, input().split()))
m = int(input())
customer = list(map(int,input().split()))

start = time.time()
for i in customer:
    if i in data:
        print('yes',end=' ')
    else:
        print('no',end=' ')
print(start - time.time())