def solution(X, Y):
    xy = set(X) & set(Y)  # 공통된 숫자 찾기

    result = [i * min(X.count(i), Y.count(i)) for i in xy]
    result = "".join(sorted(result, reverse=True))
    
    if not xy:  # 아무것도 없는 경우
        result = '-1'

    if len(xy) == 1 and '0' in xy:  # 0으로만 이루어져 있을 경우
        result = '0'

    
    return result