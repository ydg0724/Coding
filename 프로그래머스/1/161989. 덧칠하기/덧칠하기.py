def solution(n, m, section):
    cnt = 1
    start = section[0]

    for i in section:
        if start + (m-1) < i:   #다음 칠 할 범위가 벗어난 경우
            start = i
            cnt+=1

    return cnt