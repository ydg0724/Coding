def solution(nums):
    from itertools import combinations
    import math

    c = list(combinations(nums,3)) #조합
    result = 0
    for i in range(len(c)):
        c[i] = sum(c[i])
        for j in range(2, int(math.sqrt(c[i])+1)):
            chk=0
            if c[i]%j==0:
                chk=1
                break
        if chk==0:   
            result+=1


    return result