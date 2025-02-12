# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            ans = ans + abs(students[i]-seats[i])
        return ans
        