def solution(ingredient):
    takeOut = []
    answer = 0
    for i in ingredient:
        takeOut.append(i)
        if takeOut[-4:] == [1,2,3,1]:
            answer += 1
            del takeOut[-4:]

    return answer