import time
start = time.time()  # 시작 시간 저장
n,m = map(int, input().split())
a,b,d = map(int, input().split())

# 방향이동  (d + 3) % 4
# 0 : 북
# 1 : 동
# 2 : 남
# 3 : 서
sg = []
for i in range(m):
    temp = list(map(int, input().split()))
    sg.append(temp)
flag = 0
result = 1


while True:
    if flag == 4:
        flag = 0
        if d == 0:
            # 북
            a += 1
        elif d == 1:
            # 동
            b -= 1
        elif d == 2:
            # 남
            a -= 1
        elif d == 3:
            # 서
            b += 1

        if sg[a][b] == 1:
            break

    # 반시계 회전
    d = (d + 3) % 4
    if d == 0:
        # 북
        if sg[a - 1][b] == 1:
            flag += 1
            continue
        else:
            a -= 1
            sg[a][b] = 1
            result += 1
    elif d == 1:
        # 동
        if sg[a][b + 1] == 1:
            flag += 1
            continue
        else:
            b += 1
            sg[a][b] = 1
            result += 1
    elif d == 2:
        # 남
        if sg[a + 1][b] == 1:
            flag += 1
            continue
        else:
            a += 1
            sg[a][b] = 1
            result += 1
    elif d == 3:
        # 서
        if sg[a][b - 1] == 1:
            flag += 1
            continue
        else:
            b -= 1
            sg[a][b] = 1
            result += 1

    else:
        print('error')

print(result)
print("time :", time.time() - start)