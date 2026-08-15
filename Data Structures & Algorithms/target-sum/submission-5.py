class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in range(len(nums)):
            newDp=defaultdict(int)
            for curSum,count in dp.items():
                newDp[curSum+nums[i]]+=count
                newDp[curSum-nums[i]]+=count
            dp=newDp
        return dp[target]