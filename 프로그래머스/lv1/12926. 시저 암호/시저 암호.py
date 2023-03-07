def solution(s, n):
    answer = []
    lists = list(s)
    for i in lists:
        if ord(i)==32:
            answer.append(i)
        elif 65<=ord(i)<=90:
            i = ord(i)+n
            if(i>90):
                i-=26
            answer.append(chr(i))
        elif 97<=ord(i)<=122:
            i = ord(i)+n
            if(i>122):
                i-=26
            answer.append(chr(i))
    answer = "".join(answer)
    
    return answer