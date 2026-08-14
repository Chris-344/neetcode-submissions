class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxArr=[1]*len(nums)
        for i in range(len(nums)):
            for c in range(i):
                if nums[i]>nums[c]:
                    maxArr[i]=max(maxArr[i],1+maxArr[c])
        return max(maxArr)