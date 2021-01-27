n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

max = data[n-1]
n_max = data[n-2]

result = 0
t_cnt = 0
k_cnt = 0

while True:
    result+=max
    t_cnt+=1
    k_cnt+=1

    if k_cnt == k:
        k_cnt = 0
        t_cnt+=1
        result+=n_max

    if t_cnt == m:
        break

print(result)

