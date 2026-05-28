class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberTable = {}

        for i in range(len(nums)):
            if target - nums[i] in numberTable:
                if numberTable[target - nums[i]] > i:
                    return [i, numberTable[target-nums[i]]]
                else:
                    return [numberTable[target-nums[i]], i]
            else:
                numberTable[nums[i]] = i