import sys
input = sys.stdin.readline
game = {'Y':2, 'F':3, 'O':4}

play_user = {}

n, game_type = map(str, input().split())

result = 0
join = 1
for _ in range(int(n)):
    user_name = input()
    if user_name not in play_user:
        play_user[user_name] = 1
        join += 1
    if join == game[game_type]:
        join = 1
        result += 1
print(result)