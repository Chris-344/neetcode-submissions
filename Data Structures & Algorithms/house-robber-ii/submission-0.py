class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        def helper(arr):
            if len(arr)<=2:
                return max(arr)
            maxValArr=[0]*len(arr)
            for i in range(len(arr)):
                if i==0:
                    maxValArr[0]=arr[0]
                    continue
                if i==1:
                    maxValArr[1]=max(arr[:2])
                    continue
                maxValArr[i]=max(maxValArr[i-2]+arr[i],maxValArr[i-1])
            return maxValArr[-1]
        
        return max(helper(nums[:len(nums)-1]),helper(nums[1:len(nums)]))