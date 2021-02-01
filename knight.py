import time
start = time.time()  # 시작 시간 저장
p = input()

result = 0

if (ord(p[0]) + 2) <= ord('h'):
    if (int(p[1]) + 1) <= 8:
        result += 1
    if (int(p[1]) - 1) > 0:
        result += 1

if (ord(p[0]) - 2) >= ord('a'):
    if (int(p[1]) + 1) <= 8:
        result += 1
    if (int(p[1]) - 1) > 0:
        result += 1

if int(p[1]) + 2 <= 8:
    if(ord(p[0]) + 1) <= ord('h'):
        result += 1
    if(ord(p[0]) - 1) >= ord('a'):
        result += 1

if int(p[1]) - 2 > 0:
    if(ord(p[0]) + 1) <= ord('h'):
        result += 1
    if(ord(p[0]) - 1) >= ord('a'):
        result += 1

print(result)
print("time :", time.time() - start)