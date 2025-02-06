# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count_list1 = {list1[i]:i for i in range(len(list1))}
        count_list2 = {list2[i]:i for i in range(len(list2))}
        print(count_list1,count_list2)
        ans=[]
        minimum=len(list1)+len(list2)
        print(count_list1.keys(),count_list2.keys())
        for key1 in count_list1.keys():
            if key1 in count_list2.keys():
                minimum=min(minimum,count_list1[key1]+count_list2[key1])
        print(minimum)
        for key1 in count_list1.keys():
            if key1 in count_list2.keys() and minimum == count_list1[key1]+count_list2[key1]:
                ans.append(key1)

        
        return ans


        