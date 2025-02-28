import re


def solution(files):
    answer = []
    names = []

    for file in files:
        names.append(re.split(r'(\d+)', file))  # 정규식 참고
    # 	[['F-', '5', ' Freedom Fighter'], ['B-', '50', ' Superfortress'], ['A-', '10', ' Thunderbolt II'], ['F-', '14', ' Tomcat']]

    return answer