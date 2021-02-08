def bs(array, target, start, end):
    if start > end:
        return None;
    # // : 소수점 버리는 나누기
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    # 타겟이 더 작으면 앞부분 비교
    elif array[mid] > target:
        return bs(array, target, start, mid - 1)
    # 타겟이 더 크면 뒷부분 비교
    else:
        return bs(array, target, mid+1, end)
    
n, target = map(int, input().split())
array = list(map(int, input().split()))

result = bs(array, target, 0, n-1)

if result == None:
    print('타겟 없음')
    
else:
    print(str(result+1) + "번째 원소에 "+ str(target) +"이 있다")
