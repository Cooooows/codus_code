n = int(input())
k = list(map(int, input().split()))

d = [0] * n

d[0] = k[0]
d[1] = max(k[0],k[1])

i = 2
while i != n:
    # 이걸 어케 세우지?!?!?!?!?!!??!!???? 난 멍청한가?!?!?!!!!?!?! 그냥 초기값을 주면 되잖아!??!!?!!!? 앞에선 줘놓고 왜얘는 안준거야?!?!?!!?!?
    d[i] = max(d[i-1],d[i-2]+k[i])
    i += 1

print(d[n-1])

# # 몰라 걍 망
# i = 0
# result = 0
# temp = 0
# while i != n:
#
#     temp = max(temp+k[i+2],temp+k[i+3])
#     i = i+2 if k[i+2] > k[i+3] else i+3
#     print(i)
#


