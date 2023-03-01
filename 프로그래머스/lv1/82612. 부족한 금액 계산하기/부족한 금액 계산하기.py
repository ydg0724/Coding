def solution(price, money, count):
    cnt=1
    sums=0
    while count >=cnt:
        sums += price*cnt
        cnt = cnt+1
    if sums <= money:
        return 0
    else:
        return sums-money
        