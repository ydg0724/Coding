def solution(keymap, targets):
    answer = []
    for word in targets:   #한 단어
        cnt = 0
        for char in word:     #각 단어의 문자
            chk = False
            time = 101
            for key in keymap:
                if char in key: #단어가 존재한다면
                    time = min(key.index(char)+1,time)  #여러 keymap값들중 가장 작은 값
                    chk = True

            if not chk:
                cnt = -1
                break
            cnt += time
        answer.append(cnt)
    
    return answer