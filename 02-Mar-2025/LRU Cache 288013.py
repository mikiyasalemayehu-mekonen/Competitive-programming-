# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left  ,self.right = Node(0,0),Node(0,0)
        self.left.next , self.right.prev = self.right , self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            # Remove the node from its current position
            node.prev.next, node.next.prev = node.next, node.prev
            
            # Move node to MRU position
            prev, nexts = self.right.prev, self.right
            prev.next = nexts.prev = node
            node.prev, node.next = prev, nexts

            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            node.prev.next, node.next.prev = node.next, node.prev
            
            node.val = value
        else:
            if len(self.cache) == self.cap:

                lru = self.left.next
                self.left.next = lru.next
                lru.next.prev = self.left
                del self.cache[lru.key]

            node = Node(key, value)
            self.cache[key] = node

        prev, nexts = self.right.prev, self.right
        prev.next = nexts.prev = node
        node.prev, node.next = prev, nexts


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)