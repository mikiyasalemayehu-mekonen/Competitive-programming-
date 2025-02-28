# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self,val="" ,prev = None ,next = None ):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        new_node = ListNode(url, prev=self.curr)
        self.curr.next = new_node 
        self.curr = new_node  
    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val    
        
    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)