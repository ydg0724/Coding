# 라이브러리

문제 풀 때 알면 좋은 라이브러리들 정리

## itertools

- 주로 순열, 조합을 사용할 때 쓰이는 라이브러리이다.

```py
from itertools import permutations #순열
from itertools import combinations #조합
from itertools import combinations_with_replacement #중복 조합

data = ['A','B','C']

resultP = list(permutations(data, 3))
resultC = list(combinations(data, 2))
resultCR = list(combinations_with_replacement(data,2))
```
