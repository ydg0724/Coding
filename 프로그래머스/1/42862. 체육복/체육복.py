def solution(n, lost, reserve):
    tmp = reserve
    for i in range(1, n+1):
        if i not in lost:  # 잃어버린 학생이 아닌 경우는 패스
            continue
        if (i in lost) and (i in reserve):  # 잃어버린 학생이 도난 당했을 경우
            lost.remove(i)
            tmp.remove(i)
            continue
        if i-1 in tmp:  # 앞의 학생한테 빌렸을 경우
            tmp.remove(i-1)
            lost.remove(i)
            continue
        elif (i+1 in tmp) and (i+1 not in lost):  # 뒤의 학생한테 빌렸을 경우
            tmp.remove(i+1)
            lost.remove(i)
            continue

    answer = n-len(lost)
    return answer