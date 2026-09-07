class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))

        for i in range(len(nums)):
            if i==0:
                dp[i]=nums[0]
                continue
            if i==1:
                dp[i]=max(nums[1],nums[0])
                continue
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])

        return dp[-1]