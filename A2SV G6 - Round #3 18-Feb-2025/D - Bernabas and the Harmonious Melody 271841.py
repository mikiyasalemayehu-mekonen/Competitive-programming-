# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    notes = input()
   

    if notes == notes[::-1]:  
        print(0)
        continue

    left, right = 0, n - 1
    while left < right and notes[left] == notes[right]:  
        left += 1
        right -= 1
    def min_removals(notes, left, right, ch):
        l, r = left, right
        removals = 0
        while l < r:
            if notes[l] == notes[r]:  
                l += 1
                r -= 1
            elif notes[l] == ch:  
                l += 1
                removals += 1
            elif notes[r] == ch:  
                r -= 1
                removals += 1
            else:
                return float('inf')  
        return removals
    char1, char2 = notes[left], notes[right]
    result = min(min_removals(notes, left, right, char1), min_removals(notes, left, right, char2))

    print(result if result != float('inf') else -1)



