def solution(x):
    ha = []
    n=x
    while(n!=0):
        ha.append(n%10)
        n = n//10
    an = sum(ha)
    if(x%an==0):
        return True
    else:
        return False
    