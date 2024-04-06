n, k = map(int, input().split())
lists = list(map(int, input().split()))
lists.sort()
 
if k!=0 and k!=n:
    if lists[k-1] != lists[k]:
        print(lists[k-1])
    else:
        print(-1)
elif k==n:
    print(lists[k-1])
else:
    if lists[0]>1:
        print(lists[0]-1)
    else:
        print(-1)  
