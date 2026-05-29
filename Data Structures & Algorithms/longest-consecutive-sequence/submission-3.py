class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        longestSequence = 1
        currentSequence = 1
        for num in nums:
            if num-1 in nums:
                currentSequence = 2
                while(num-1+currentSequence) in nums:
                    currentSequence+=1
                longestSequence = max(longestSequence, currentSequence)

        longestSequence = max(longestSequence, currentSequence)
        return longestSequence
        