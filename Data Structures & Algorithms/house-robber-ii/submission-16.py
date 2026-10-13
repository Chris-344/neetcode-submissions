class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self,arr):
        maxArr=[0]*len(arr)
        for i in range(len(arr)):
            if i==0:
                maxArr[i]=arr[0]
                continue
            if i==1:
                maxArr[i]=max(arr[:2])
                continue
            maxArr[i]=max(maxArr[i-2]+arr[i],maxArr[i-1])
        return maxArr[-1]