class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp=[0]*2
        temp[0]=celsius+273.15
        temp[1]=(celsius*1.80)+32
        return temp
