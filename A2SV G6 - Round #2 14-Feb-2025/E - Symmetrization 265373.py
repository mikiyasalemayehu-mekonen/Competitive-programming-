# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

n = int(input())
for _ in range(n):
    m = int(input())
    matrice = []
    for i in range (m):
        temp = list(map(int,input()))
        matrice.append(temp)

    count = 0
    for row in range(m):
        for col in range(m):
            temp = [matrice[row][col],matrice[col][m-row-1],matrice[m-row-1][m-col-1],matrice[m-col-1][row]]
            count = count + min(temp.count(0),temp.count(1))

    print(count//4)
    


    