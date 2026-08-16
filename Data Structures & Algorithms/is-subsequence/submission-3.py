class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if not s:
            return True
        for i in range(len(t)):
            if len(s)==j:
                return True
            if t[i]==s[j]:
                j+=1
        return j==(len(s)) 