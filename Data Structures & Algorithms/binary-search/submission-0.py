class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo <=hi:
            m=lo+(hi - lo)//2
            if target > nums[m]:
                lo=m+1
            elif target <nums[m]:
                hi=m-1
            else:
                return m
        return -1