class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftPtr = 0
        rightPtr = len(nums) - 1
        while (leftPtr <= rightPtr):
            middlePtr = (leftPtr+rightPtr)//2
            if (nums[middlePtr]) == target:
                return middlePtr
            elif (target > nums[middlePtr]):
                leftPtr = middlePtr+1
            else:
                rightPtr = middlePtr-1
        
        return -1
        