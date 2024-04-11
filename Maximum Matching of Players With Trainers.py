class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        index1=0
        index2=0
        ans=0
        while index1<len(players) and index2<len(trainers):
            if players[index1]<=trainers[index2]:
                ans+=1
                index1+=1
                index2+=1
            else:
                index2+=1
        return ans


        
