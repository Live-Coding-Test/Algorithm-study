from itertools import combinations_with_replacement

n = int(input())

numbers = [1, 5, 10, 50]

arr = set([sum(_) for _ in combinations_with_replacement(numbers, n)])

print(len(arr))