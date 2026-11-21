class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        i, n = 0, len(intervals)
        res = []
        while i < n and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        
        res.append([s, e])
        res.extend(intervals[i:])
        return res

                
