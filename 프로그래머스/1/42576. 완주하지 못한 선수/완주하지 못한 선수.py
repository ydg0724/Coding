def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):    #정렬하고 같은 인덱스에 있지 않으면 리턴
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant)-1] #끝까지 안나오면 마지막 요소 리턴
