class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        def helper(nums:list[int])->int:
            if len(nums) == 1:
                return nums[0]

            if tuple(nums) in cache:
                return cache[(tuple(nums))]

            returns = []
            for i in range(len(nums)):
                if i-1<0:
                    left = 1
                else:
                    left = nums[i-1]
                if i+1 == len(nums):
                    right = 1
                else:
                    right = nums[i+1]

                this_return = nums[i] * left * right
               
                temp_val = nums.pop(i)
                result = this_return + helper(nums)
                returns.append(result)
                nums.insert(i,temp_val)
            cache[tuple(nums)] = max(returns)
            
            return max(returns)
        
        return helper(nums)
