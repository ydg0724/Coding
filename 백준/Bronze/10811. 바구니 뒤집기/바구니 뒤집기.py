m,n = map(int,input().split())

answer = []
for i in range(m):
    answer.append(i+1)

for i in range(n):
    i,j = map(int,input().split())
    tmp = answer[i-1:j]
    tmp.reverse()
    answer[i-1:j] = tmp

for i in answer:
    print(i,end=" ")