def solution(n, arr1, arr2):
    answer = []
    a=[]
    for i in range(n):
        a.append(bin(arr1[i]|arr2[i])[2:].zfill(n))
        b = a[i].replace('0',' ').replace('1','#')
        answer.append(b) 
        
    
    return answer