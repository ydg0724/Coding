def solution(name, yearning, photo):
    matching = {}   #딕셔너리 생성
    answer = []
    for i in range(len(name)):
        matching[name[i]] = yearning[i] #딕셔너리 키 값 매핑
    for i in range(len(photo)):
        sums = 0
        for j in photo[i]:
            if j in matching.keys():
                sums += matching[j]
        answer.append(sums)



    return answer