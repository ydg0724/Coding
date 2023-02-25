def solution(s):
    di = len(s)
    answer = ''
    if di%2==0:
        answer = s[di//2-1]+s[di//2]
    else:
        answer = s[di//2]
    return answer