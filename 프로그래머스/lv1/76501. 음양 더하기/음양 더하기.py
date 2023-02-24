def solution(absolutes, signs):
    tmp = []
    answer = 1
    for i in range(len(signs)):
        if(signs[i] == False):
            absolutes[i] = -absolutes[i]
    answer = sum(absolutes)    
    return answer