def solution(sizes):
    a=[]
    b=[]
    for i in range(len(sizes)):
        a.append(max(sizes[i]))
        b.append(min(sizes[i]))
    answer = max(a)*max(b)

    return answer