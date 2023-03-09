from itertools import combinations
def solution(number):
    a = list(combinations(number,3))
    answer=0
    for i in a:
        if sum(i)==0:
            answer = answer+1
    return answer