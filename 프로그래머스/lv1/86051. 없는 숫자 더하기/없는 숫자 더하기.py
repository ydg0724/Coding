def solution(numbers):
    i=0
    lis = []
    while(i<10):
        if i not in numbers:
            lis.append(i)
        i=i+1
    answer = sum(lis)
    return answer