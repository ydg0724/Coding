def solution(n):
    thr=[]
    answer=0
    while n>0:
        thr.append(n%3)
        n = n//3
    for i in range(len(thr)):
        answer += thr[i]*(3**(len(thr)-i-1))
    
    return answer