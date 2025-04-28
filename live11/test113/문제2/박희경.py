import sys

input = sys.stdin.readline

n = int(input())
feed = []
feed_dict = {}
for _ in range(n):
    data = input().split()

    feed.append(data[1:])

    layer = feed_dict
    for f in feed:
        if f not in layer:
            layer[f] = {}
        layer = layer[f]
print(feed_dict)
        


"""
3
2 B A
4 A B C D
2 A C

4
2 KIWI BANANA
2 KIWI APPLE
2 APPLE APPLE
3 APPLE BANANA KIWI
"""