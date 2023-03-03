def solution(s):
    answer = []
    lists = s.split(' ')
    for i in lists:
        tmp = []
        for j in range(len(i)):
            if j%2==0:
                tmp.append(i[j].upper())
            else:
                tmp.append(i[j].lower())
        answer.append(''.join(tmp))
    answer = ' '.join(answer)
    return answer