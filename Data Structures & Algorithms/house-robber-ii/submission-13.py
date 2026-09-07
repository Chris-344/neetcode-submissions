class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:len(nums)-1]))

    def helper(self,arr):
        if not len(arr):
            return 0
        if len(arr)==1:
            return arr[0]
        
        h1=arr[0]
        h2=max(arr[0],arr[1])
        for i in range(2,len(arr)):
            tmp=max(h1+arr[i],h2)
            h1=h2
            h2=tmp
        return h2