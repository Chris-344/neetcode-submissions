class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=nums[0]
        l,r = 0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m] >= nums[r]:
                mini=min(mini,nums[m])
                l=m+1
            else:
                mini=min(mini,nums[m])
                r=m-1
        return mini
        #  2 1
        #  m=1