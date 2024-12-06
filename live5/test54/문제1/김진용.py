n = int(input())
s = set()
result = 0
for _ in range(n):
    string = input()
    if string == "ENTER":
        result += len(s)
        s.clear()
    else:
        s.add(string)
result += len(s)
print(result)
