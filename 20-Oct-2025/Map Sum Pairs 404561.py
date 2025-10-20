# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        self.sum = 0
class MapSum:

    def __init__(self):
        self.map = {} 
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0) 
        node = self.root
        node.sum += diff
        self.map[key]=val
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sum += diff
        

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
            
        return node.sum



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

       

    # def insert(self, key: str, val: int) -> None:
    #     diff = val - self.map.get(key, 0)  # handle re-insert with different value
    #     self.map[key] = val

    #     node = self.root
    #     # node.sum += diff  # update root sum
    #     for c in key:
    #         if c not in node.children:
    #             node.children[c] = TrieNode()
    #         node = node.children[c]
    #         # node.sum += diff
    #     # node.value = val

    
    