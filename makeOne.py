x = int(input())
result = 0

t = [0] * (30001)

t[1] = 1
t[2] = 1
t[3] = 1
t[4] = 2
t[5] = 1
t[30000] = 30000
n = 6

if x >= 6:
    while n != (x+1):
        a = 30000
        b = 30000
        c = 30000
        d = 30000

        if n % 5 == 0:
            a = n // 5

        if n % 3 == 0:
            b = n // 3

        if n % 2 == 0:
            c = n // 2

        d = n - 1

        t[n] = min(t[a],t[b],t[c],t[d]) + 1

        n += 1


print(t[x])


# # topdown얘도 망
# d = []
#
# for i in range(x+1):
#     d.append(list())
#
# def one(n):
#     d[n].append(n-1)
#
#     if n % 5 == 0:
#         d[n].append(n // 5)
#         one(n // 5)
#     elif n % 3 == 0:
#         d[n].append(n // 3)
#         one(n // 3)
#
#     elif n % 2 == 0:
#         d[n].append(n // 2)
#         one(n // 2)
#
#     one(n-1)
#
#     print(d[n])
#
# one(x)


# # topdown
# def one(n):
#     if x == 1:
#         return 1
#
#     if d[n] != 0:
#         return d[n]
#
#     d[n] =
#

# # 걍 망한거
# while x != 1:
#     if x % 5 == 0:
#         x /= 5
#     elif x % 3 == 0:
#         x /= 3
#     elif x % 2 == 0:
#         x /= 2
#     else:
#         x -= 1
#     result += 1
#     print(x, result)