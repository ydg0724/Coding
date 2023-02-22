def solution(s):
    answer = True
    if(s.count('p') + s.count('P') == s.count('y')+s.count('Y')):
        return True
    elif(s.count('p')+s.count('P')==0 and s.count('y')+s.count('Y')==0):
        return True
    else:
        return False
