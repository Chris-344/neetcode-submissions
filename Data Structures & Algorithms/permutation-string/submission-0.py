class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        m1=defaultdict(int)
        m2=defaultdict(int)
        for ch in range(len(s1)):
            m1[s1[ch]]=1 + m1.get(s1[ch],0)
            m2[s2[ch]]=1 + m2.get(s2[ch],0)

        matches=26
        
        for ch in "qwertyuiopasdfghjklzxcvbnm":
            if m1[ch]!=m2[ch]:
                matches-=1
        
        
        l=0
        for i in range(len(s1),len(s2)):
            if matches==26:return True
            
            left=s2[l]
            right=s2[i]

            m2[right]+=1
            if m1[right]==m2[right]:
                matches+=1
            elif m1[right]+1==m2[right]:
                matches-=1
            
            m2[left]-=1
            if m1[left]==m2[left]:
                matches+=1
            elif m1[left]-1==m2[left]:
                matches-=1
            
            l+=1
        return matches==26