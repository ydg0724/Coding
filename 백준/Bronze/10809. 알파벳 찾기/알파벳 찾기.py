words = input()

lists = 'abcdefghijklmnopqrstuvwxyz'

for i in lists:
    if i in words:
        print(words.index(i), end=" ")
    else:
        print(-1, end=' ')
