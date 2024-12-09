# 테스트 케이스 -> t
#
# n, m <- n: 문서 개수, m: 궁금한 문서가 현재 몇 번째
#
# 1 1 9 1 1 1
#
# set 이용? 튜플이라고 했나 그건가
#

#
# 1
# (0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)
#
# (1, 1), (2, 9), (3, 1), (4, 1), (5, 1), (0, 1)
#
# (2, 9), (3, 1), (4, 1), (5, 1), (0, 1), (1, 1),

test = int(input())

for t in range(test):
    n, m = map(int, input().split())
    ary = list(map(int, input().split()))

    ary_2 = []
    for i in range(len(ary)):
        ary_2.append((i, ary[i]))

    ary.sort(reverse=True)

    cnt = 0

    while ary_2:
        max_ip = max(ary)

        if ary_2[0][1] < max_ip:
            ary_2.append(ary_2.pop(0))

        elif ary_2[0][1] == max_ip:
            cnt += 1

            if ary_2[0][0] == m:
                print(cnt)
                break
            else:
                ary_2.pop(0)
                ary.pop(0)

