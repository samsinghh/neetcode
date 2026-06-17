class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = []
        nums = [-num for num in nums]
        heapq.heapify(nums)
        self.maxHeap = nums
        self.k = k 

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, -val)
        temp = []
        for _ in range(self.k - 1):
            value = heapq.heappop(self.maxHeap)
            temp.append(value)
        res = -1 * self.maxHeap[0]
        for num in temp:
            heapq.heappush(self.maxHeap, num)
        return res

        
