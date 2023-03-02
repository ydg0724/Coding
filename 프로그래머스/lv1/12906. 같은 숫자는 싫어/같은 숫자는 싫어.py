def solution(arr):
    answer = [arr[0]]
    stack = []
    for i in arr:
        if stack:
            tmp = stack.pop()
            if tmp!=i:
                answer.append(i)
        stack.append(i)    
    return answer