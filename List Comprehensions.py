if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    nums=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                num=[]
                if i+j+k!=n:
                    num.append(i)
                    num.append(j)
                    num.append(k)
                    nums.append(num)
    print(nums)
