class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            buckets[count-1].append(num)
        
        res = []
        while len(res) < k:
            for i in range(len(buckets) - 1, -1, -1):
                for j in range(len(buckets[i])):
                    res.append(buckets[i][j])
                    if len(res) == k:
                        return res
        
        return res
