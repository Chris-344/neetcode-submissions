class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        curr=[]
        def dfs(i):
            if i>len(nums):
                return
            if i==len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            
            j=i+1
            while j<len(nums) and nums[i]==nums[j]:
                j+=1
            dfs(j)
        dfs(0)
        return res