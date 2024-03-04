def solution(s):
    seperate = []
    seper_part = ''
    first_cnt = 0
    else_cnt = 0

    x = 0
    for i in s:
        seper_part += i
        if x == 0 or x == i:    # 첫 번째 글자 저장 or 첫 번째 글자와 같은 경우
            x = i
            first_cnt += 1
        else:                   # 첫 번째 글자 외의 문자
            else_cnt += 1

        if first_cnt == else_cnt:  # 횟수가 같아지는 경우
            seperate.append(seper_part)
            x = first_cnt = else_cnt = 0
            seper_part = ''
    answer = len(seperate)
    if (seper_part != ''):  # 마지막에 남아있는 문자열이 있다면
        answer += 1
    return answer