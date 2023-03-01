def solution(n, m):
    answer = []
    i=1
    while i<n or i<m:
        if n%i==0 and m%i==0:
            mx = i
        i=i+1
    i=mx
    cn = True
    while cn:
        if i%n==0 and i%m==0:
            mn = i
            cn=False
        i += mx
    answer.append(mx)
    answer.append(mn)
    return answer