def solution(dartResult):
    answer=0
    square = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    score = ''
    result = []
    for i in dartResult:
        if i.isdigit(): #숫자인 경우 score에 추가
            score+=i

        elif i in square:  #보너스
            result.append(int(score) ** square[i])
            score = ''
        elif i=='#': #옵션(아차상)
            result[-1] *= -1
        elif i=='*': #옵션(스타상)
            result[-1] *= 2
            if len(result)>=2:
                result[-2] *=2

    answer = sum(result)

    return answer