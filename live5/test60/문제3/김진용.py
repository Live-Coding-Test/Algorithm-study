def solution(s):
    cnt = s.count('1')

    while bin(cnt)[2:] != 1:



print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
