class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for num in nums:
            if num in numberSet: return True
            numberSet.add(num)
        
        return False