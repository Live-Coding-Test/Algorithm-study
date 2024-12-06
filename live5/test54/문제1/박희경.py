import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
member = set()

for _ in range(n):
    chat = input().rstrip()
    if chat == "ENTER":
        cnt += len(member)
        member.clear()
        continue

    member.add(chat)

cnt += len(member)
print(cnt)
