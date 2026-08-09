class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        mySet=set()
        res=0
        while r<len(s):
            if s[r] in mySet:
                while s[r] in mySet and l<r:
                    mySet.remove(s[l])
                    l+=1
            mySet.add(s[r])
            res=max(res,r-l+1)
            r+=1
        return res