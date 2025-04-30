import sys

input = sys.stdin.readline

n = int(input())

layer_dict = {}
for _ in range(n):
    data = input().split()

    layer = layer_dict
    for feed in data[1:]:
        if feed not in layer:
            layer[feed] = {}
        layer = layer[feed]
        

def printer(layer_dict, layer):
    layer_list = sorted(list(layer_dict))
    for i in layer_list:
        print('--' * layer, end='')
        print(i)
        printer(layer_dict[i], layer + 1)

printer(layer_dict, 0)
