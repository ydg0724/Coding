def solution(left, right):
    plus = []
    minus = []
    
    for i in range(left,right+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j==0:
                cnt = cnt+1
        if cnt%2==0:
            plus.append(i)
        else:
            minus.append(i)      
    answer = sum(plus) - sum(minus)
    return answer