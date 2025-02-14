# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n , m =map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
count = 0
ptr1 = 0
ptr2 = 0
ans  = []
for i in range(len(list2)):
    while ptr1<n and list2[i] > list1[ptr1]:
        count = count + 1
        ptr1 = ptr1  + 1
    ans.append(count)
    
print(*ans)