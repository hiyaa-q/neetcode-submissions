class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returnTable = []

        i = 0
        while i < len(nums)-2:
            leftPtr = i+1
            rightPtr = len(nums)-1
            while(leftPtr < rightPtr):
                sumOf = nums[i]+nums[leftPtr]+nums[rightPtr]
                if sumOf == 0:
                    returnTable.append([nums[i], nums[leftPtr], nums[rightPtr]])
                    leftPtr+=1
                    while (nums[leftPtr] == nums[leftPtr-1] and leftPtr < rightPtr):
                        leftPtr += 1
                elif sumOf > 0:
                    val = nums[rightPtr]
                    rightPtr-=1
                    while (rightPtr > i and nums[rightPtr] == val):
                        rightPtr-=1
                else:
                    val = nums[leftPtr]
                    leftPtr+=1
                    while (leftPtr < len(nums) and nums[leftPtr] == val):
                        leftPtr+=1

            val = nums[i]
            i+=1
            while (i < len(nums)-2 and nums[i] == val):
                i+=1
                
        
        return returnTable;