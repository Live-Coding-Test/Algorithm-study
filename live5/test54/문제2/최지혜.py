import sys
input = sys.stdin.readline

N, X = map(int,input().split())
blog = list(map(int, input().split()))

inter_sum = 0 # X일 동안의 방문자 합
max_blog = -1
cnt = 0


# 만약 모든 방문자가 0이라면, SAD를 출력
if max(blog) == 0:
    max_blog = 0

else:
    # 첫 X일 동안의 합 초기화
    inter_sum = sum(blog[:X]) 
    max_blog = inter_sum
    cnt = 1

    # 시작점을 한 칸씩 오른쪽으로 이동하며 합 갱신
    for start in range(X, N):
        inter_sum -= blog[start-X] # 이전 시작점의 값을 빼기
        inter_sum += blog[start] # 새로운 끝점의 값을 더하기

        if inter_sum > max_blog: # 새로운 최대값을 찾은 경우
            max_blog = inter_sum
            cnt = 1
        elif inter_sum == max_blog: # 현재 최대값과 같은 경우
            cnt += 1
    
if max_blog == 0:
    print('SAD')
else:
    print(max_blog)
    print(cnt)
