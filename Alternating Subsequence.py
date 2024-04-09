n=int(input())
for i in range(n):
    size=int(input())
    lists=list(map(int,input().split()))
    temp=[]
    temp.append(lists[0])
    index=0
    for j in range(1,len(lists)):
        if temp[-1] * lists[j] < 0 :
            temp.append(lists[j])
            index+=1
        elif temp[index]<lists[j]:
            temp[index]=lists[j]
        else:
            continue
    print(sum(temp))
