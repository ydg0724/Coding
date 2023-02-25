def solution(n):
    i=0
    tmp = []
    if n%2==0:
        while n>i:
            tmp.append('수박')
            i=i+2
    else:
        while n>i:
            tmp.append('수')
            i=i+1
            if n==i:
                break
            tmp.append('박')
            i=i+1
    answer = "".join(tmp)
    return answer