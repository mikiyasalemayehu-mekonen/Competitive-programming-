class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lists=[[a,b] for a,b in zip(position,speed)]
        stack=[]
        sort = sorted(lists, key=lambda x: x[0], reverse=True)
        for pos,spe in sort:
            stack.append((target-pos)/spe)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
