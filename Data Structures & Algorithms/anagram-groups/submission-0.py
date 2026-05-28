class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringMap = {}
        for string in strs:
            anagramical = [0]*26
            for char in string: anagramical[ord(char)-ord('a')] += 1
            if tuple(anagramical) in stringMap:
                stringMap[tuple(anagramical)].append(string)
            else:
                stringMap[tuple(anagramical)] = [string]
        
        return list(stringMap.values())
        