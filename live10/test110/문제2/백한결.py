import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    craneWeight = list(map(int, input().split()))
    M = int(input())
    boxWeight = list(map(int, input().split()))

    boxWeight.sort(reverse=True)
    craneWeight.sort(reverse=True)

    if boxWeight[0] > craneWeight[0]:
        print(-1)
        return

    time = 0

    while boxWeight:
        index = 0
        i = 0

        while index < N and i < len(boxWeight):
            if craneWeight[index] >= boxWeight[i]:
                boxWeight.pop(i)
                index += 1
            else:
                i += 1
        time += 1

    print(time)


if __name__ == '__main__':
    main()