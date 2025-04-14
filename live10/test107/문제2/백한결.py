def main():
    N, D = map(int, input().strip().split())

    route = []

    for _ in range(N):
        start, end, length = map(int, input().split())
        if end > D:
            continue
        route.append((start, end, length))

    dist = [i for i in range(D+1)]

    for i in range(D+1):
        if i+1 <= D:
            dist[i+1] = min(dist[i+1], dist[i]+1)

        for start, end, length in route:
            if start == i:
                dist[end] = min(dist[end], dist[start] + length)

    print(dist[D])




if __name__ == "__main__":
    main()