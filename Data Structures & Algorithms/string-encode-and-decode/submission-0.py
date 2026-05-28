class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = [str(len(strs))]

        for string in strs:
            prefix.append("_" + str(len(string)))
        prefix.append("_")

        return "".join(prefix) + "".join(strs)

    def decode(self, s: str) -> List[str]:
        startIndex = s.find("_")
        returnList = []
        stringCount = int(s[0:startIndex])
        sizeList = []

        if stringCount == 0: return returnList

        for i in range(stringCount):
            endIndex = s.find("_", startIndex+1)
            sizeList.append(int(s[startIndex+1:endIndex]))
            startIndex = endIndex

        for i in range(stringCount):
            returnList.append(s[startIndex+1:startIndex+1+sizeList[i]])
            startIndex += sizeList[i]

        return returnList
