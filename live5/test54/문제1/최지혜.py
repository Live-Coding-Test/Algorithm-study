import sys
n = int(sys.stdin.readline())
gom = set()
cnt = 0

for _ in range(n):
    user = sys.stdin.readline().strip()
    if user == 'ENTER': 
        cnt += len(gom)
        gom = set() # 곰곰티콘 이용 수를 count하고 초기화 
    else:
        gom.add(user)

cnt += len(gom)
print(cnt)