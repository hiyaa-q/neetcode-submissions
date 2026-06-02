class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while (leftPtr < rightPtr and numbers[leftPtr] + numbers[rightPtr] != target):
            if numbers[leftPtr] + numbers[rightPtr] < target:
                leftPtr+=1
            else:
                rightPtr-=1
        
        return [leftPtr+1, rightPtr+1]