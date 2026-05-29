class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = [nums[0]]
        postfixArray = [nums[len(nums)-1]]
        for i in range(1, len(nums)):
            j = len(nums) - i - 1
            prefixArray.append(nums[i]*prefixArray[i-1])
            postfixArray.append(nums[j]*postfixArray[i-1])

        solutionArray = [postfixArray[len(nums)-2]]
        for i in range(1, len(nums)-1):
            solutionArray.append(prefixArray[i-1]*postfixArray[len(nums)-2-i])
        solutionArray.append(prefixArray[len(nums)-2])

        return solutionArray
        