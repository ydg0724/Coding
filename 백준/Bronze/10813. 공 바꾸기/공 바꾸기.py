N,M = map(int, input().split())


answer = []
for i in range(N):
    answer.append(i+1)

for _ in range(M):
    i,j = map(int, input().split())
    tmp = answer[i-1]
    answer[i-1] = answer[j-1]
    answer[j-1] = tmp

for i in answer:
    print(i ,end = " ")