class Solution:
    def rob(self, nums: List[int]) -> int:
        maxArr=[0]*(len(nums))

        for i in range(len(nums)):
            if i==0:
                maxArr[i]=nums[i]
                continue
            if i==1:
                maxArr[i]=max(nums[0],nums[1])
                continue
            maxArr[i]=max(maxArr[i-2]+nums[i],maxArr[i-1])

        return maxArr[-1]