def bs(array, target, start, end):
    mid = (start + end) // 2
    while True:
        if start > end:
            return None
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = map(int, input().split())
array = list(map(int, input().split()))



