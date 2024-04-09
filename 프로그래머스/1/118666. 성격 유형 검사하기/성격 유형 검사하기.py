from collections import defaultdict

def solution(survey, choices):
    


    result = ""
    dict_int = defaultdict(int)
    mbti = ['RT', 'CF', 'JM', 'AN']

    choice_score = {
        1: 3,
        2: 2,
        3: 1,
        4: 0,
        5: 1,
        6: 2,
        7: 3
    }

    for i in range(len(survey)):
        # 점수 배점 순서 지정
        neg, pos = survey[i][0], survey[i][1]

        # 점수 배열
        if choices[i] < 4:
            dict_int[neg] += choice_score[choices[i]]
        if choices[i] > 4:
            dict_int[pos] += choice_score[choices[i]]

    for i in mbti:
        if dict_int[i[0]] > dict_int[i[1]] or dict_int[i[0]] == dict_int[i[1]]:
            result += i[0]
        else:
            result += i[1]
            
    return result
