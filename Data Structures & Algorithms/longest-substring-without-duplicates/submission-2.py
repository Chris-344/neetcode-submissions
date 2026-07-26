class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet=set()
        res=0
        l=0
        r=0
        
        while r < len(s):
            while s[r] in mySet and l <= r:
                mySet.remove(s[l])
                l+=1
            mySet.add(s[r]) 
            r+=1
        
            res=max(res,len(mySet))
        return res


"""
have 2 pointers left and right
move right forward and put it in the set
if an element in rs position is in the set move the left pointer
forward and make sure that ls current letter is removed
do this while the letter is the same as right 
now keep moving right forward
do this till the end
"""