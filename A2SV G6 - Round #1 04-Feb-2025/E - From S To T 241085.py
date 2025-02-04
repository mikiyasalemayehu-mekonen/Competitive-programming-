# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

n=int(input())
for i in range(n):
    s=list(input())
    t=list(input())
    p=list(input())
    temp=""
    ptr1=0
    ptr2=0
    while ptr2<len(t):
        if s and t[ptr2]==s[0]:
            ptr2+=1
            s.remove(s[0])
        elif t[ptr2] in p:
            p.remove(t[ptr2])
            ptr2+=1
        else:
            break
    if len(s)==0 and ptr2==len(t):      
        print("YES")
    else:
        print("NO")