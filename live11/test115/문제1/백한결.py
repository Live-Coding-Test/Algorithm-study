import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    A = [int(input()) for _ in range(n)]

    v = [A[0]]
    for x in A[1:]:
        if x != v[-1]:
            v.append(x)

    H = max(v)

    ans = H - v[0]
    for i in range(1, len(v)):
        if v[i] < v[i-1]:
            ans += (v[i-1] - v[i])
    print(ans)

if __name__ == "__main__":
    main()