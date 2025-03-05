n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer = arr1 + arr2
answer.sort()

print(*answer)