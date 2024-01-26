def solution(cards1, cards2, goal):
    answer = ''
    word = []
    
    for i in goal:
        if i == cards1[0]: #cards1에 있는 경우
            word.append(i)
            del cards1[0]
            if len(cards1) == 0:
                cards1.append(1)
        elif i == cards2[0]:    #cards2에 있는 경우
            word.append(i)
            del cards2[0]
            if len(cards2) == 0:
                cards2.append(1)
        else:
            answer = 'No'
            break

    if word == goal:
        answer = 'Yes'
    else:
        answer = 'No'

    return answer
