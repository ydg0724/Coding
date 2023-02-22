def solution(n):
    sqrt = n ** (1/2)
    
    if(sqrt %1==0):
        answer = (sqrt +1)**2
    else:
        answer = -1
    
    return answer