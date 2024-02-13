# 효율적인 코드

알고리즘 문제를 풀면서 알게된 시간복잡도를 줄이는 방법을 정리

## 약수 구하기

문제: https://school.programmers.co.kr/learn/courses/30/lessons/136798

```py
def getMyDivisor(n):
    divList = []

    for i in range(1, int(n**(1/2) + 1 )):
        if n%i == 0:
            divList.append(i)
            if( (i**2) != n)    #N=A*B, A==B가 아닌 경우 ex)25=5*5
                divList.append(n // i)

    divList.sort()
    return divList
```

- N = A\*B로 나타낼 수 있다는 것을 이용한 풀이이다.
- for문을 이용해 자연수 N의 제곱근까지 약수를 구하면 그 짝이 되는 약수는 자동으로 구할 수 있다.
- 일반적인 for문을 이용하면 O(N)이지만 이 방법은 O(N^(1/2))이 된다.
