# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C


n = int(input())
for _ in range(n):
    length = int(input())
    word = list(input())

    set_1 = set()
    right_count = [0]*length
    index_1 = 0

    for char in word:
        if char not in set_1:
            set_1.add(char)
        right_count[index_1] = len(set_1)
        index_1 +=1
        if index_1>=length:
            break
    
    set_2 = set()
    left_count = [0]*length
    index_2 = 0
    for i in range(length-1,-1,-1):
        if word[i] not in set_2:
            set_2.add(word[i])
        left_count[i] = len(set_2)
    maximum = 0
    for i in range(length-1):
        maximum = max(maximum,right_count[i]+left_count[i+1])

    print(maximum)
