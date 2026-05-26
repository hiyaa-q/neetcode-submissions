class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}

        for letter in s:
            if letter in letterMap:
                letterMap[letter] += 1
            else:
                letterMap[letter] = 1
        
        for letter in t:
            if letter not in letterMap: return False

            letterMap[letter] -= 1
            if letterMap[letter] <= 0: del letterMap[letter]

        return (not letterMap)