t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a_ary = list(map(int, input().split()))
    b_ary = list(map(int, input().split()))
    # print(a_ary, b_ary)
    a_ary.sort()
    b_ary.sort()


    # print(a_ary, b_ary)

    def eat(eater):
        start = 0
        end = len(b_ary) - 1
        c = -1  # 한 쌍도 없을 경우를 위해 -1로 초기화
        while start <= end:
            mid = (start + end) // 2
            if b_ary[mid] < eater:
                c = mid
                start = mid + 1
            else:
                end = mid - 1
        return c + 1


    cnt = 0
    for i in a_ary:
        cnt += eat(i)
    print(cnt)

#
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _t in range(t):
#     n, m = map(int, input().split())
#     a_ary = list(map(int, input().split()))
#     b_ary = list(map(int, input().split()))
#     # print(a_ary, b_ary)
#     a_ary.sort()
#     b_ary.sort()
#     # print(a_ary, b_ary)
#
#
#     def eat(eater):
#         global result
#         start = 0
#         end = len(b_ary) - 1
#
#         while start <= end:
#             mid = (start + end) // 2
#             if b_ary[mid] < eater:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#         return len(b_ary[:start])
#
#     cnt = 0
#     for i in a_ary:
#         result = 0
#         cnt += eat(i)
#     print(cnt)