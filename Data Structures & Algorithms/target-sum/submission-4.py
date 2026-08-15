class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in range(len(nums)):
            newDp=defaultdict(int)
            for cur_sum,count in dp.items():
                newDp[cur_sum+nums[i]]+=count
                newDp[cur_sum-nums[i]]+=count
            dp=newDp
        return dp[target]