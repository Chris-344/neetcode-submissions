class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total/2

        def dfs(i,curSum):
            if curSum==target:
                return True
            if i>=len(nums) or curSum>target:
                return
            return dfs(i+1,curSum+nums[i]) or dfs(i+1,curSum)


        if dfs(0,0):
            return True
        return False