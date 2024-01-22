# 파이썬 간단한 문법 정리

파이썬 기본 문법 정리

## 문자열 메소드

- s.len() -> 문자열 개수 반환
- s.upper() -> 대문자로 변환
- s.lower() -> 소문자로 변환
- s.title() -> 각 단어의 앞글자만 대문자 변환
- s.capitalize() -> 첫 문자를 대문자로 변환
- s.count('a') -> 'a'의 개수 반환
- s.find('a') -> 'a'가 왼쪽부터 몇 번째있는지 반환
- s.rfind('a') -> 'a'가 오른쪽부터 몇 번째있는지 반환
- s.startswith('a') -> 'a'로 시작하는지 여부 반환
- s.endswith('a') -> 'a'로 끝나는지 여부 반환
- s.strip() -> 좌우 공백 삭제 (lstrip,rstrip -> 좌,우)
- s.split('\n') -> \n을 기준으로 나누어 리스트로 반환
- s.isdigit() -> 문자열의 숫자 여부 반환
- s.islower() -> 문자열의 소문자 여부 반환
- s.isupper() -> 문자열의 대문자 여부 반환

## 입력 함수

```py
a, b, c, d = map(int, input().split())

data = list(map(int,input().split()))
#map함수는 객체를 반환하므로 list로 묶어줘야함
```

## 출력 함수(print)

- %서식 -> %자료형 %(값)

print("%d %d %d" %(1,2,3)) print("%s %s %s" %('a','b','c'))

- format() 함수 -> '{자료형}'.format(인수)

print("{0},{1:.2f}".format(10,10.555))

## 리스트 관련 메소드

- a.append(value)
- a.insert(index,value)
- a.clear()
- del a[index]
- a.remove(value)
- a.pop(index)
- len(a)
- a.count(value)
- b = a.copy()
- a.extend(b) -> a에 b값 추가
- a.index(index)
- a.sort() or a.sort(reverse=True)
- a.reverse()
- a.replace(a,b) -> a를 b로 교체

## 튜플 or 세트

- set.union() intersection() difference()
- a.add(x)
- a.remove(x) or a.discard
- a.pop
- a.clear()
- len(a)

## 딕셔너리

- a.['a'] = 1 (딕셔너리 추가)
- a.keys()
- a.values()
- a.items()

## 람다식

```py
#기본 문법
lambda 매개변수 : 리턴값

def plus(x,y):
   return x + y
print(plus(1, 10))

print((lambda x, y: x + y)(1,10))

lists = [1, 2, 3, 4, 5]
```

```py
#응용(내장함수)
array = [('홍길동',50), ('이순신',32), ('아무개', 74)]

def my_key(x):
   return x[1]
print(sorted(array,key=my_key))
print(sorted(array,key=lambda x:x[1]))
# 튜플의 두번째 원소를 기준으로 정렬
```

```py
#응용(여러 개의 리스트)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = list(map(lambda a, b : a+b, list1, list2))
```
