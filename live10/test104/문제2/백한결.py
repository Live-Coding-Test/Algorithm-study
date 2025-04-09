# 2-친구가 되는법
# 1. A와 B가 친구
# 2. A와 B는 친구가 아니지만 공통친구 C가 존재

def main():
    N = int(input())
    A = [input().strip() for _ in range(N)]

    friendsList = set()
    numFriend = []

    for i in range(N):
        for j in range(N):
            for k in range(N):
               if i == j:
                   continue
               if A[i][j] == 'Y':
                   friendsList.add(j)
               else:
                   if A[k][i] == 'Y' and A[k][j] == 'Y':
                       friendsList.add(j)
        numFriend.append(len(friendsList))
        friendsList.clear()

    print(max(numFriend))

if __name__ == "__main__":
    main()