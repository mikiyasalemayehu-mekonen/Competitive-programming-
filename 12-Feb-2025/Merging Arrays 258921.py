# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int,input().split())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
ptr1 = 0
ptr2 = 0
ans  = []
while ptr1<n and ptr2<m:
    if num1[ptr1]<=num2[ptr2]:
        ans.append(num1[ptr1])
        ptr1+=1
    else :
        ans.append(num2[ptr2])
        ptr2+=1

if ptr2 < m:
    ans.extend(num2[ptr2:])
if ptr1 < n:
    ans.extend(num1[ptr1:])

print(*ans)


    