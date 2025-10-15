# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        temp = self.trie
        for c in word:
            if c not in temp:
                temp[c] = {}
            temp = temp[c]
        temp['#'] = True

    def search(self, word: str) -> bool:
        temp = self.trie
        n = len(word)
        def  s(i,tem):
            if i == n: 
                return '#' in tem
            t  = False
            if word[i]==".":
                for k in tem.keys():
                    if k != '#' and s(i + 1, tem[k]):
                        return True
                   
            if word[i] not in tem:
                return False
            else:
                t = t or s(i+1,tem[word[i]])
            return t

        
        return s(0,temp)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)