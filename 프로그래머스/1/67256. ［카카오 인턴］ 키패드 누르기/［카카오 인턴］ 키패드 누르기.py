def solution(numbers, hand):
    # https://school.programmers.co.kr/learn/courses/30/lessons/67256

    result = ""
    keyPad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    #   1   2   3
    #   4   5   6
    #   7   8   9
    #   *   0   #

    leftHand = keyPad['*']
    rightHand = keyPad['#']
    for press in numbers:
        curPos = keyPad[press]
        if press in [1, 4, 7]:
            result += 'L'
            leftHand = keyPad[press]
        elif press in [3, 6, 9]:
            result += 'R'
            rightHand = keyPad[press]
        else:
            # 손과 버튼과의 거리
            lDist = abs(leftHand[0] - curPos[0]) + abs(leftHand[1] - curPos[1])
            RDist = abs(rightHand[0] - curPos[0]) + abs(rightHand[1] - curPos[1])

            if lDist > RDist: #오른손이 가까운 경우
                result +='R'
                rightHand = keyPad[press]
            elif RDist > lDist: #왼손이 가까운 경우
                result += 'L'
                leftHand = keyPad[press]
            else:           #거리가 같은 경우
                if hand == 'right':
                    result +='R'
                    rightHand = keyPad[press]
                else:
                    result += 'L'
                    leftHand = keyPad[press]
                    
    return result