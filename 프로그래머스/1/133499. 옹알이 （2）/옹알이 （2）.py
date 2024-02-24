def solution(babbling):
    says = [ "aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        for i in says:
            if i*2 not in word: #2번 중복해서 나오지 않을 경우
                word = word.replace(i,' ')  #babbling 단어를 공백으로 바꿈
    
        if word.isspace():  #babbing단어가 전부 공백으로 될 시에 answer+=1
            answer+=1
    return answer