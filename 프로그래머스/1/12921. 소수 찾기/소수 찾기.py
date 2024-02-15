def solution(n):
    import math


    result = 0
    for i in range(2,n+1):
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j==0:
                break
        else:
            result+=1
            
    return result
