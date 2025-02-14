# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

rows,cols = map(int,input().split())
dir = []
field = []
flag = "YES"

dir=[(0,1),(0,0),(1,1),(1,0),(-1,0),(-1,-1),(0,-1),(-1,1),(1,-1) ]
for _ in range(rows):
    temp = list( input())
    field.append(temp)
for row in range(rows):
    for col in range(cols):
        count = 0 

        for i,j in dir:
            if 0<=row+i < rows and 0<=col+j < cols:
                x = row + i 
                y = col + j
                if field[x][y]=="*":
                    count = count + 1
        if  field[row][col] == "." and count>0:
            flag = "NO"
            break
        elif field[row][col] == "." and count==0:
            continue
        elif  field[row][col] != "." and (field[row][col] != "*" and count != int(field[row][col])): 
            flag = "NO"
            break
    if flag =="NO":
        break

print(flag)
    
                



