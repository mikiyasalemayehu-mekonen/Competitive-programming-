# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        

    def add(self, num: int) -> None:
        if self.nums[-1] ==0 :
            self.nums = [1]
            self.nums.append(num)
        else:
            self.nums.append(self.nums[-1]*num)


    def getProduct(self, k: int) -> int:
        if k>len(self.nums)-1:
            return 0
        elif k+1<=len(self.nums):
            return self.nums[-1]//self.nums[-k-1]
        else:
            return self.nums[-1]
         

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)