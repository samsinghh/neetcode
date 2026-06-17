class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        mapper = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            counts[num] += 1

        for num in counts:
            mapper[counts[num]].append(num)
        
        res = []
        for i in range(len(mapper)-1, 0, -1):
            for num in mapper[i]:
                res.append(num)
                if len(res) == k:
                    return res