class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s) - 1

        while (leftPtr < rightPtr):
            while(leftPtr < len(s) and not s[leftPtr].isalnum()):
                leftPtr+=1
            while(rightPtr >= 0 and not s[rightPtr].isalnum()):
                rightPtr-=1
            if (leftPtr > rightPtr): return True
            
            if (s[leftPtr].lower() != s[rightPtr].lower()): return False
            leftPtr += 1
            rightPtr -= 1
        
        return True