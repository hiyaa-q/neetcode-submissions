class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        leftPtr = 0
        rightPtr = len(s) - 1

        while (leftPtr < rightPtr):
            while(leftPtr < len(s) and not s[leftPtr].isalnum()):
                leftPtr+=1
            while(rightPtr >= 0 and not s[rightPtr].isalnum()):
                rightPtr-=1
            if (leftPtr > rightPtr): return True

            leftChar = s[leftPtr]
            rightChar = s[rightPtr]
            
            if (leftChar != rightChar): return False
            leftPtr += 1
            rightPtr -= 1
        
        return True