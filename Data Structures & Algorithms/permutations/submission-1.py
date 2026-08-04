class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]

        perms=self.permute(nums[1:])
        res=[]
        for i in range(len(perms)):
            for j in range(len(perms[0])+1):
                curr_copy=perms[i].copy()
                curr_copy.insert(j,nums[0])
                res.append(curr_copy.copy())
        
        return res