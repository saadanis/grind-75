class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        final_interval = []
        new_start, new_end = newInterval
        i = 0

        while i < len(intervals) and intervals[i][1] < new_start:
            final_interval.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i += 1

        final_interval.append([new_start, new_end])

        return final_interval + intervals[i:]