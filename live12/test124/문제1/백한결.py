import sys

def main():
    input = sys.stdin.readline
    S = input().strip()
    P = input().strip()

    Slen = len(S)
    Plen = len(P)
    i = 0
    count = 0

    while i < Plen:
        maxLen = 0

        for j in range(len(S)):
            k = 0
            while i + k < Plen and j + k < Slen and P[i + k] == S[j + k]:
                k += 1
            maxLen = max(maxLen, k)

        i += maxLen
        count += 1

    print(count)


if __name__ == '__main__':
    main()