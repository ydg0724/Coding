def solution(N, stages):
    down = len(stages) #실패율의 분모
    failure = []
    for i in range(N):
        n = stages.count(i+1)   #실패율 분자 찾기
        if down!=0:
            failure.append(n/down)
        else:
            failure.append(0)
        down -= n

    result = []
    for i in range(N):
        maxIndex = failure.index(max(failure))  #가장 큰 실패율의 인덱스 추출
        result.append(maxIndex+1)
        failure[maxIndex] = -1

    return result