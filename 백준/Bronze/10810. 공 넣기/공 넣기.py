N,M = map(int, input().split())


answer = []
for i in range(N):
    answer.append(0)

for _ in range(M):
    i,j,k = map(int, input().split())
    start = i-1
    end = j
    for a in range(start,end):
        answer[a] = k

for i in answer:
    print(i ,end = " ")