def solution(s, skip, index):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    s = list(s)
    for i in skip:
        alpha.remove(i)
    for i in range(len(s)):  # skip 삭제
        s[i] = alpha[(alpha.index(s[i])+index) % len(alpha)] #s[i]에서 index를 더한 만큼 삽입
    
    s = ''.join(s)  #다시 문자열화
    return s