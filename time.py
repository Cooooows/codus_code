n = int(input())
result = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)


# 1분 : 0 ~ 59
# 3은 3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53 -> 1분에 15번
# 1시간 : 0 ~ 59분 -> 1시간에 '3'이 들어간 분이 15번 -> 15*60
# 1시간 : (45 * 15) + (15 * 60)
#
# 15 + (45 * 15) 번
# 3시, 13시, 23시 : 3600번


# result = 0
#
# if n < 3:
#     result = (n+1) * (45 * 15) + (15 * 60)
#
# elif n < 13:
#     result = (n) * (45 * 15) + (15 * 60) + 3600
#
# elif n < 23:
#     result = (n - 1) * (45 * 15) + (15 * 60) + (3600 * 2)
#
# else:
#     result = (n - 2) * (45 * 15) + (15 * 60) + (3600 * 3)
#
# print(result)