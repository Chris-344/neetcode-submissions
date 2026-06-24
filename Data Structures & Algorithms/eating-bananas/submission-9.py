class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed=max(piles)
        l=1
        r=max(piles)

        while l<=r:
            m=l+(r-l)//2

            total=0
            for i in piles:
                total+=math.ceil(i/m)
            if total<=h:
                speed=min(speed,m)
                r=m-1
            else:
                l=m+1
            
        return speed


        # 1 2  4  5 6
        # 4
        #