class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        ml,mr=height[l],height[r]

        total=0

        while l < r:
            if ml <= mr:
                l+=1
                ml=max(height[l],ml)
                total+=ml-height[l]
            elif ml > mr:
                r-=1
                mr=max(height[r],mr)
                total+=mr-height[r]
        return total