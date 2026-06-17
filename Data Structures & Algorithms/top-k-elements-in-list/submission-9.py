class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            freqs[num] += 1
        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res


                    
        
