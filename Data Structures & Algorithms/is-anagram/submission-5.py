class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj={}
        obj2={}
        for i in s:
            if i not in obj:
                obj[i]=1
            else:
                obj[i]+=1
        for j in t:
            if j not in obj2:
                obj2[j]=1
            else:
                obj2[j]+=1

        return obj==obj2