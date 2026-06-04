class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        returnValue = 0
        leftPointer = 0

        for rightPointer in range(1, len(prices)):
            profit = prices[rightPointer] - prices[leftPointer]
            returnValue = max(returnValue, profit)
            
            if (prices[rightPointer] < prices[leftPointer]):
                leftPointer = rightPointer

        return returnValue
        