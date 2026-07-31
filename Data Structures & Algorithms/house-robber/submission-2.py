class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        maxValArr=[0]*len(nums)

        for i in range(len(nums)):
            if i==0:
                maxValArr[i]=nums[i]
                continue
            if i==1:
                maxValArr[i]=max(nums[0:1])

            maxValArr[i]=max(maxValArr[i-2]+nums[i],maxValArr[i-1])

        return maxValArr[len(maxValArr)-1]