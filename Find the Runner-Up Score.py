if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrList=list(arr)
    arrList.sort()
    n=len(arrList)-1
    temp=arrList[n]
    for j in range (n-1,-1,-1):
        if temp>arrList[j]:
            print(arrList[j])
            break
