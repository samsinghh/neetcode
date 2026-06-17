class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        res = []
        sorted_arr = sorted(counts.items(), key=lambda x:x[1])
        temp = sorted_arr[-1*k:]
        for item in temp:
            res.append(item[0])
        return res
