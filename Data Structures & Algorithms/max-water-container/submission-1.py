class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(heights)-1
        maxArea = 0
        while (leftPtr < rightPtr):
            area = (rightPtr-leftPtr)*min(heights[leftPtr], heights[rightPtr])
            maxArea = max(maxArea, area)
            if (heights[rightPtr] < heights[leftPtr]):
                rightPtr-=1
            else:
                leftPtr+=1

        return maxArea