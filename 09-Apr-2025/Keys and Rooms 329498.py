# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        n=len(rooms)
        def dfs(node,visited):
            visited.add(node)
            for nieghours in rooms[node]:
                if nieghours  not in visited:
                    dfs(nieghours ,visited)
            return 
        dfs(0,visited)
        return len(visited)==n