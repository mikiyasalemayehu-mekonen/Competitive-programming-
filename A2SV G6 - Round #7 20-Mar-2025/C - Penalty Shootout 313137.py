# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

n = int(input())
for _  in range(n):
    penality = list(input())
    team1 = 0
    team2 = 0
    i = 0
    while i<10:
        if  penality[i]=="1" and i%2==0 :
            team1 = team1 + int(penality[i])
        elif  penality[i]=="1" and i%2!=0:
            team2 = team2 + int(penality[i])
        elif penality[i]=="?":
            if i%2==0:
                team1 = team1 + 1
        if i%2==0 and (team1)>(team2 + (10-i)//2 ):
            
            break
        if i%2==0 and (team1 +  ((10-i)//2) - 1 )<(team2):
            break
        if i%2!=0 and (team1 + (10-i-1)//2)<(team2):
            break
        if i%2!=0 and (team1)>(team2+((10-i-1)//2)):
            break
        i = i + 1
    
        

    ans1 = i + 1 if i<10 else 10
    team1 = 0
    team2 = 0
    i = 0
    while i<10:
        if  penality[i]=="1" and i%2==0 :
            team1 = team1 + int(penality[i])
        elif  penality[i]=="1" and i%2!=0:
            team2 = team2 + int(penality[i])
        elif penality[i]=="?":
            if i%2!=0:
                team2 = team2 + 1
        if i%2==0 and (team1)>(team2 + (10-i)//2 ):
            
            break
        if i%2==0 and (team1 +  ((10-i)//2) - 1 )<(team2):
            break
        if i%2!=0 and (team1 + (10-i-1)//2)<(team2):
            break
        if i%2!=0 and (team1)>(team2+((10-i-1)//2)):
            break
        i = i + 1
    
        

    ans2 = i + 1 if i<10 else 10

    print(min(ans1,ans2))