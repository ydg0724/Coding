def solution(a, b):
    answer =''
    days = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    if a==1:
        answer = days[b%7]
    else:
        for i in range(a-1):
            sum += month[i]
        answer = days[(sum+b)%7]
    return answer