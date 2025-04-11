def main():
    n = int(input())
    m = int(input())

    cityMap = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        cityMap[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().strip().split())
        cityMap[a-1][b-1] = min(c, cityMap[a-1][b-1])


    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                cityMap[j][k] = min(cityMap[j][k], cityMap[j][i] + cityMap[i][k])

    for row in cityMap:
        print(' '.join(str(x if x != float('inf') else 0) for x in row))

if __name__ == "__main__":
    main()