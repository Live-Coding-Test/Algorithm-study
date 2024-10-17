def solution(sequence, k):
    a, b = 0, 0
    ary = [0, len(sequence)]
    total = sequence[0]
    while True:
        if total < k:
            b += 1
            if b == len(sequence): break
            total += sequence[b]
        elif total >= k:
            if total == k:
                if ary[1] - ary[0] > b - a:
                    ary = [a, b]
            total -= sequence[a]
            a += 1

    return ary