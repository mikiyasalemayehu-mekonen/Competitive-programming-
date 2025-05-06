# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small = [] 
        self.large = [] 
        

    def addNum(self, num: int) -> None:
        heappush(self.small,-num)
        heappush(self.large,-(heappop(self.small)))
        if  len(self.small)<len(self.large):
            heappush(self.small,-(heappop(self.large)))

            
        
    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            temp = (-(self.small[0]) + self.large[0])/2
            return temp
        return -self.small[0]
     

 
     


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()