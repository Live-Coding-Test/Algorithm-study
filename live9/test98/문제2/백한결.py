from itertools import permutations

def main():
    x = str(input().strip())

    # 모든 순열 생성
    perm = set(permutations(x))

    # 가능한 후보 중 x보다 큰 수
    candidates = []
    for p in perm:
        numStr = ''.join(p)
        num = int(numStr)
        if num > int(x):
            candidates.append(num)

    if candidates:
        print(min(candidates))
    else:
        print(0)

if __name__ == "__main__":
    main()