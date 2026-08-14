class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2:
            return False        
        target=total/2
        mySet=set()
        mySet.add(0)

        for i in range(len(nums)-1,-1,-1):
            newSet=set()
            for n in mySet:
                if (n+nums[i])==target:
                    return True
                newSet.add(n+nums[i])
                newSet.add(n)
            mySet=newSet

        return target in mySet