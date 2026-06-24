class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxL=0
        strs=set()
#1233
        while r < len(s):
            while s[r] in strs:
                strs.remove(s[l])
                l+=1
            strs.add(s[r])

            maxL=max(maxL,len(strs))
            r+=1
        return maxL