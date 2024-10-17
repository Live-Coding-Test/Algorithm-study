ary_size = int(input())

ary = []

for i in range(ary_size):
    ary.append(int(input()))
ary.sort()
# print(ary)
temp = []
for i in ary:
    cnt = 0
    for j in range(i, i + 5):
        if j not in ary:
            cnt += 1
    temp.append(cnt)
print(min(temp))
