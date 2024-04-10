class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans=0
        people.sort()
        first=0
        last=len(people)-1
        while first<=last:
            if people[last]==limit:
                ans+=1
                last-=1
            else:
                if people[last]+people[first] <=limit:
                    ans+=1
                    first+=1
                    last-=1
                else:
                    ans+=1
                    last-=1
       
        return ans
