def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda a:a[n])
    return answer