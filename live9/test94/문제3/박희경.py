def solution(stones, k):
    answer = 0

    left, right = 1, max(stones)        # 나올 수 있는 stones 원소의 최대값
    while left <= right:
        cnt = 0
        mid = (left + right) // 2       
        for stone in stones:
            if stone <= mid:            # mid가 더 크거나 같은 경우 => 0인 경우
                cnt += 1
            else:  cnt = 0              # 0 아닌 경우 다시 0 개수 카운팅
            if cnt >= k: break
        if cnt < k:                     # mid가 큰 경우가 적었다는 뜻이니 더 크게 만들기
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
            
    return answer