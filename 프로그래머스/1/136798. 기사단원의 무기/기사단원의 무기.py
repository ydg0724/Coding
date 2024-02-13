def solution(number, limit, power):
    div = []
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**(1/2)+1)):
            if (i % j == 0):
                if j == i//j:  # 제곱근일 경우
                    cnt += 1
                else:           #그냥 약수
                    cnt += 2
        div.append(cnt)

    for i in range(len(div)):
        if div[i] > limit:
            div[i] = power

    return sum(div)