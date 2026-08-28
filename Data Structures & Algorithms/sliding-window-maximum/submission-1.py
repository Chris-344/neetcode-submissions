class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res=[]
        window=[]

        for i,n in enumerate(nums):
            heapq.heappush(window,(-n,i))
            if i+1<k:
                continue
            while window[0][1]<i-k+1:
                heapq.heappop(window)
            res.append(-window[0][0])        

        return res