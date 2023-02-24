def solution(phone_number):
    answer = ''
    star = len(phone_number)-4
    tmp = list(phone_number)
    for i in range(star):
        tmp[i] = '*'
    answer = ''.join(tmp)
    print(tmp)
    return answer