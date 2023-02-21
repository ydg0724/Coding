def solution(n):
    answer = 0
    i=1
    prime = []
    while(i<=n):
        if(n%i==0):
            prime.append(i)
        i=i+1
    answer = sum(prime)
    return answer