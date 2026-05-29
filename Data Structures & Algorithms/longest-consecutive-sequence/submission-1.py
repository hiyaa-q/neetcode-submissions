class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        
        longestSequence = 1
        currentSequence = 1
        previousNumber = nums[0]
        i = 1
        while (i < len(nums)):
            while(i < len(nums) and nums[i] == previousNumber):
                i+=1
            if (i >= len(nums)):
                print("aborted")
                break

            print(nums[i])
            if nums[i] == previousNumber+1:
                print("yay")
                currentSequence+=1
            else:
                longestSequence = max(longestSequence, currentSequence)
                currentSequence = 1
            
            previousNumber = nums[i]
            i+=1

        longestSequence = max(longestSequence, currentSequence)
        return longestSequence
        