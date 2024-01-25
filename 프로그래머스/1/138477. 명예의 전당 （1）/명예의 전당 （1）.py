def solution(k, score):
    answer = []
    presentation = []
    for i in score:
        if len(presentation) < k: #맨 처음 k까지 명예의 전당 자동 등록
            presentation.append(i)
            presentation.sort()
            answer.append(presentation[0])
        else:
            if i < presentation[0]: #명예의 전당에 들지 못하는 경우
                answer.append(presentation[0])
                continue
            else:
                presentation.append(i)
                presentation.sort()
                if len(presentation) > k:
                    del presentation[0]
                answer.append(presentation[0])
    return answer