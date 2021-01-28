# 숫자 카드
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

# 그럼 행중ㅇ에 가장 작은수를 모두 뽑아서 그중에 가장 큰수를 뽑으라는거?

# n, m 입력
n,m = map(int, input().split())

#data 입력
for i in range(0,n):
    data = list(map(int, input().split()))
    temp = min(data)
    min_num = 99999
    if temp < min_num:
        min_num = temp

print(min_num)
