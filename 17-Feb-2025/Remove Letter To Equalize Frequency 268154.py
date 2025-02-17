# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        def check(freq):
            test_val = list(count.values())[0]
            res = all(val == test_val for val in count.values())
            return res

        count = Counter(word)
        for i in range(len(word)):
            count[word[i]] = count[word[i]] - 1
            if count[word[i]]==0:
                count.pop(word[i])
            if check(count):
                return True
            else:
                count[word[i]] = count[word[i]] + 1

             
        return False


        