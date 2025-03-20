import itertools


def solution(k, dungeons):
    answer = -1

    counts = []

    p = itertools.permutations(dungeons, len(dungeons))

    for i in p:
        counts.append(maxDungeons(k, i))

    counts.sort()

    return counts[-1]


def maxDungeons(k, dungeons):
    count = 0
    health = k

    for dungeon in dungeons:
        if dungeon[0] > health:
            break
        else:
            count += 1
            health -= dungeon[1]

    return count
