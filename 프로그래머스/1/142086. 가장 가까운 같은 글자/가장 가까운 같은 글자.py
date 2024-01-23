def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            while s[:i].count(s[i])>1:
                s = s.replace(s[i],'1',1)
            answer.append(i-s.find(s[i]))
        else:
            answer.append(-1)

    return answer