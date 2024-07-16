class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        player1=[]
        player2=[]
        def predict(nums, is_player1_turn, player1, player2):
            if not nums:
                return sum(player1) >= sum(player2)
            if is_player1_turn:
                choice1 = nums[0]
                choice2 = nums[-1]
                return (predict(nums[1:], False, player1 + [choice1], player2) or
                        predict(nums[:-1], False, player1 + [choice2], player2))
            else: 
                choice1 = nums[0]
                choice2 = nums[-1]
                return (predict(nums[1:], True, player1, player2 + [choice1]) and
                        predict(nums[:-1], True, player1, player2 + [choice2]))

            return predict(new_nums, not is_player1_turn, player1, player2)
        if len(nums) % 2 == 0:
            return True
        return predict(nums, True, player1,player2)
