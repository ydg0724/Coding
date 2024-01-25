def solution(food):
    answer = ''
    n = '1'
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer += n
            
        n = str(int(n)+1)
        
    rev = answer[::-1]
    answer += '0'
    answer += rev
    
    return answer