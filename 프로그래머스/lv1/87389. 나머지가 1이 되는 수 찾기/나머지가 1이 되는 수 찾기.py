def solution(n):
    i=1
    while(n>i):
        if(n%i==1):
            return i
        i=i+1
    