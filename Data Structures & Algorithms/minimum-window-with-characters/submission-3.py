class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resMap=defaultdict(int)
        sMap=defaultdict(int)

        for c in t:
            sMap[c]+=1

        have,need=0,len(sMap)
        res,resLen=[-1,-1],float("infinity")

        l=0
        for r in range(len(s)):            
            resMap[s[r]]+=1

            if resMap[s[r]]==sMap[s[r]]:
                have+=1

            while have==need:
                if (r-l+1)<resLen:
                    res=[l,r+1]
                    resLen=(r-l+1)
                resMap[s[l]]-=1
                if resMap[s[l]]<sMap[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r] if resLen!=float("infinity") else ""