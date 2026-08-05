class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[:len(nums)-1]),self.helper(nums[1:]))

    def helper(self,nums):
        if not nums:
            return 0
        maxArr=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                maxArr[i]=nums[i]
                continue
            if i==1:
                maxArr[i]=max(nums[1],nums[0])
                continue
            maxArr[i]=max(nums[i]+maxArr[i-2],maxArr[i-1])
        return maxArr[-1]
