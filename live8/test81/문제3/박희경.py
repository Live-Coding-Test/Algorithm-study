from collections import *


def solution(records):
    result = []
    answer = []
    user = defaultdict()
    for record in records:
        cmd = list(map(str, record.split()))
        if cmd[0] != 'Leave':  # {유저 아이디: 닉네임}
            user[cmd[1]] = cmd[-1]
        if cmd[0] != 'Change':
            result.append([cmd[0], cmd[1]])

    for res in result:
        if res[0] == 'Enter':
            answer.append(user[res[1]] + "님이 들어왔습니다.")
        if res[0] == 'Leave':
            answer.append(user[res[1]] + "님이 나갔습니다.")

    return answer
