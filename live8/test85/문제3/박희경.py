def solution(clothes):
    clothes_dict = {}
    for name, kind in clothes:
        if kind in clothes_dict.keys():
            clothes_dict[kind].append(name)
        else:
            clothes_dict[kind] = [name]

    # (n + 1) * (m + 1) - 1
    answer = 1
    for key, values in clothes_dict.items():
        answer *= len(values) + 1
    return answer - 1