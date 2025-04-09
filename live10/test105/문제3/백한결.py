def solution(order):
    index = 0
    stack = []
    truck = []

    for i in range(1, len(order) + 1):
        if i == order[index]:
            truck.append(i)
            index += 1
        else:
            stack.append(i)

        while stack and stack[-1] == order[index]:
            truck.append(stack.pop())
            index += 1

    return len(truck)
