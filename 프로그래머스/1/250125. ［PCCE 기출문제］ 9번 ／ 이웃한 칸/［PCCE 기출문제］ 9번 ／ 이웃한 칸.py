def solution(board, h, w):
    answer = 0
    maxh = len(board)-1
    maxw = len(board[0])-1

    color = board[h][w]
    direction = [[-1,0],[0,-1],[1,0],[0,1]] #방향



    for H,W in direction:
        moveH = h + H
        moveW = w + W

        if (0<=moveW<=maxw) and (0<=moveH<=maxh):
            if color == board[moveH][moveW]:
                answer +=1

    return answer