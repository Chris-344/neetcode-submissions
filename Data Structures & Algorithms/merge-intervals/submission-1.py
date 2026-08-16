class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        res=[intervals[0]]

        for start,end in intervals[1:]:
            lastEn=res[-1][1]
            if start<=lastEn:
                res[-1][1]=max(end,lastEn)
            else:
                res.append([start,end])
        return res