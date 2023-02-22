def solution(n):
    a = []
    tmp=0
    answer=0
    while(n>0):
        a.append(n%10)
        n = n//10
    a.sort()
    i=0
    while(len(a)!=0):
        tmp = a[0]*(10**i)
        answer += tmp
        del a[0]
        i=i+1
    return answer