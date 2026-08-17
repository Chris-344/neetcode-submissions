class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        res=[intervals[0]]

        for i in range(len(intervals)):
            lb=intervals[i][0]

            if res[-1][1]>=lb:
                res[-1]=[res[-1][0],max(res[-1][1],intervals[i][1])]
            else:
                res.append(intervals[i])
        return res