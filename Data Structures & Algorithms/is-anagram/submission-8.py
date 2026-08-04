class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj1={}
        obj2={}
        for i in s:
            obj1[i]=1 + obj1.get(i,0)
        for j in t:
            obj2[j]=1 + obj2.get(j,0)
        return obj1==obj2