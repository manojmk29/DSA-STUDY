class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        left = 0
        right = 1
        res = 0
        
        while right < len(intervals):
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right += 1
            elif intervals[left][1] <= intervals[right][1]:
                res += 1
                right += 1
            elif intervals[left][0] <= intervals[right][0]:
                left = right
                right += 1
                res += 1
                
        return res