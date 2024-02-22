a = int(input())

for _ in range(a):
    repeat, words = input().split()
    for j in words:
        print(j*int(repeat),end='')
    print()