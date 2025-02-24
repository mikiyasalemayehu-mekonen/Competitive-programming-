# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n , k ,q = map(int,input().split())
tempreature = [0] * 200002

ranges = [] 
for i in range(n):
    t1 , t2 = map(int,input().split())
    tempreature[t1] = tempreature[t1] + 1
    tempreature[t2+1] = tempreature[t2+1] - 1

for i in range(1,200002):
    
    tempreature[i] = tempreature[i-1] + tempreature[i]

tempre_freq = [0] * 200002

for i in range(1,200002):
    if tempreature[i] >=k:
        tempre_freq[i] = tempre_freq[i-1] + 1
    else:
        tempre_freq[i] = tempre_freq[i-1]


for i in range(q):
    t1 , t2 = map(int,input().split())
    print(tempre_freq[t2] -tempre_freq[t1-1])




