def solution(num):
    cnt=1
    answer = -1
    if(num==1):
        return 0
    while(cnt<=499):
        if(num%2==0):
            num /= 2
        elif(num%2==1):
            num = num*3+1
        if(num==1):
            answer = cnt
            break
        cnt +=1
        
    return answer