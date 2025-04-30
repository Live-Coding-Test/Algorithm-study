import sys

def main():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        phoneNumber = []
        n = int(input())
        for i in range(n):
            phoneNumberStr = input().strip()
            phoneNumber.append(phoneNumberStr)

        phoneNumber.sort()

        isOk = True
        for i in range(len(phoneNumber)-1):
            if phoneNumber[i+1].startswith(phoneNumber[i]):
                print("NO")
                isOk = False
                break
        if isOk:
            print("YES")

if __name__ == '__main__':
    main()
