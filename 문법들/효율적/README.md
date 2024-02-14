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
- 일반적인 for문을 이용하면 O(N)이지만 이 방법은 O(√N)이 된다.

## 소수 구하기 (에라토스테네스의 체)

```py
import math
def prime_number(n):
    for i in range(2,int(math(n)+1)):
        if n%i == 0:
            return False

    return True
```

- 각 수가 갖는 약수는 해당 수의 제곱근을 기준으로 대칭을 이루기 때문에 2부터 제곱근까지 나누어 떨어지는지만 확인하면 된다.
- 이 경우 시간복잡도는 O(√N)이 된다.
