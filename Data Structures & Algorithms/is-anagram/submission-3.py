class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj=defaultdict()
        for i in s:
                if i in obj:
                        obj[i]+=1
                else:
                        obj[i]=1
        obj2=defaultdict()
        for j in t:
                if j in obj2:
                        obj2[j]+=1
                else:
                        obj2[j]=1
        return obj==obj2