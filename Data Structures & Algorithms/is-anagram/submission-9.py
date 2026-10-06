class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj1=Counter(s)
        obj2=Counter(t)
        if obj1==obj2:
            return True
        return False