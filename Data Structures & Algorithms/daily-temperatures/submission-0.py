class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexStack = []
        temperatureStack = []
        returnArray = []

        for curIndex in range(len(temperatures)):
            returnArray.append(0)

            curTemp = temperatures[curIndex]
            # 2 main conditions
            # monotonic decreasing stack
            # either the number at the top of the stack is smaller 
            # the number at the top of the stack is bigger
            while (temperatureStack and temperatureStack[-1] < curTemp):
                pastDay = indexStack.pop()
                returnArray[pastDay] = curIndex - pastDay
                temperatureStack.pop()
             
            indexStack.append(curIndex)
            temperatureStack.append(curTemp)

        return returnArray;
        