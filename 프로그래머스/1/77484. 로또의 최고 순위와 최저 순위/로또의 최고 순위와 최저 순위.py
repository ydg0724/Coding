def solution(lottos, win_nums):
    answer = []
    unknown_nums = lottos.count(0)  # 지워진 번호 수

    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1

    best_case = cnt + unknown_nums
    worst_case = cnt

    if best_case < 2:
        answer.append(6)
    else:
        answer.append(7-best_case)
    
    if worst_case < 2:
        answer.append(6)
    else:
        answer.append(7-worst_case)
        
    return answer
