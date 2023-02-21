def solution(n):
    answer = 0
    num = []
    while(True):
        num.append(n%10)
        n = n//10
        if(n==0):
            break
    
    answer = sum(num)
    return answer