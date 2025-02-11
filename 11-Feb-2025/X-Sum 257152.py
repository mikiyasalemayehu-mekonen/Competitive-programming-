# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

size = int(input())                                             
for _ in range(size):
    n, m = map(int,input().split())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))

    maximum = 0
    for row in range(n):
        for col in range(m):
            temp = matrix[row][col]

            x = row
            y = col
            while x>=0 and y<m:
                temp = temp + matrix[x][y]
                x = x-1
                y = y+1
        
            x = row
            y = col
            while y>=0 and x<n:
                temp = temp + matrix[x][y]
                x = x+1
                y = y-1

            x = row
            y = col
            while  x>=0 and y>=0:
                temp = temp + matrix[x][y]
                x = x-1
                y = y-1
        
            x = row
            y = col
            while x<n and y<m:
                temp = temp + matrix[x][y]
                x = x+1
                y = y+1
            temp = temp - 4*(matrix[row][col])
            maximum =max(maximum,temp)
    print(maximum)
