from collections import defaultdict

def main():
    n, m = map(int, input().split())

    countryMap = defaultdict(list)

    for _ in range(m):
        A_i, B_i, C_i = map(int, input().strip().split())
        countryMap[A_i].append(C_i)
        countryMap[B_i].append(C_i)

if __name__ == "__main__":
    main()