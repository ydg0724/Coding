def solution(board, moves):
    basket = [-1]
    answer = 0

    for mv_num in moves:  # moves 순회
        for col in range(len(board)):   # num의 열들 검사
            if board[col][mv_num-1] != 0:  # 열들에 0이 아닌 숫자(인형이 있는 경우)
                if board[col][mv_num-1] == basket[-1]:  # 이미 basket 맨 위에 있는 경우
                    basket.pop()
                    answer += 2
                else:  # basket에 없는 경우 basket에 추가
                    basket.append(board[col][mv_num-1])
                board[col][mv_num-1] = 0  # 뽑은 인형은 0으로 변경
                break
    return answer