def solution(elements):
    prefix_sum = [0] * (len(elements) + 1)
    sums = set()

    for i in range(len(elements)):
        prefix_sum[i + 1] = prefix_sum[i] + elements[i]

    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            end = (start + length) % len(elements)

            # 일반적인 수열이므로 end까지의 합에서 start까지의 합을 뺌
            if start < end:
                part_sum = prefix_sum[end] - prefix_sum[start]
            # 원형 수열이므로 전체의 합에서 start까지의 합을 빼고 end까지를 더함
            else:
                part_sum = (prefix_sum[len(elements)] - prefix_sum[start]) + prefix_sum[end]
            sums.add(part_sum)

    return len(sums)