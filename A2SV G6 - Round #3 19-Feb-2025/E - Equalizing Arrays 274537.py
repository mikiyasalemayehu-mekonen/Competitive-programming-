# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
list1 = list(map(int,input().split()))
k = int(input())
list2 = list(map(int,input().split()))
for i in range(1,n):
    list1[i] = list1[i-1] + list1[i]

for i in range(1,k):
    list2[i] = list2[i-1] + list2[i]

ptr1 = 0
ptr2 = 0
count = 0
while ptr1<n and ptr2<k:
    if list1[ptr1] == list2[ptr2]:
        count  = count + 1
        ptr1 = ptr1 + 1
        ptr2 = ptr2  + 1
    elif list1[ptr1] < list2[ptr2]:
        ptr1  = ptr1 +  1
    else:
        ptr2  = ptr2 +  1

if ptr1<n or ptr2<k:
    print(-1)
else:
    print(count)



    



