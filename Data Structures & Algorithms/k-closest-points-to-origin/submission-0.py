class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        arr=[]
        for x,y in points:
            arr.append([x**2+y**2,x,y])
        heapq.heapify(arr)
        while k>0:
            [a,b,c]=heapq.heappop(arr)
            res.append([b,c])
            k-=1
        return res