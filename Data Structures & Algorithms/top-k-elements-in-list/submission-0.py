class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        buckets = [[] for i in range(len(nums))]

        for n in nums:
            frequencyMap[n] = frequencyMap.get(n, 0) + 1
        for n, s in frequencyMap.items():
            buckets[s-1].append(n)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result