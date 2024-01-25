def solution(a, b, n):
    answer = 0
    rate = b/a #교환 비율

    while n >= a:
        give = (n//a)*a  # 반납하는 병 수
        receive = (give * b) / a #받는 병 수

        n = n - give + receive  #정산 후 남은 병

        answer += receive   #받은 병 기록

    return answer