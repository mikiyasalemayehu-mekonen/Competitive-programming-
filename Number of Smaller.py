n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
count = 0
ans = []
 
for i in range(len(list2)):
    while count < n and list2[i] > list1[count]:
        count += 1
    ans.append(count)
 
for j in range(len(ans)):
    print(ans[j], end=" ")
    
