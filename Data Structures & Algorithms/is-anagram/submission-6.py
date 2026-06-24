class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj={}
        obj2={}

        for c in s:
            if c in obj:
                obj[c]+=1
            else:
                obj[c]=0
        
        for ch in t:
            if ch in obj2:
                obj2[ch]+=1
            else:
                obj2[ch]=0
        
        return obj==obj2