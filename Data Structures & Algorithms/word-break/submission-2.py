class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
    def addWord(self,word):
        curr=self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isEnd=True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root=TrieNode()
        for w in wordDict:
            root.addWord(w)
        dp={}
        
        def dfs(i,curr,word):
            if (i,curr,word) in dp:
                return dp[i,curr,word]
            if i==len(s) and curr.isEnd:
                return True
            if i>=len(s) or s[i] not in curr.children:
                return False

            word+=s[i]
            curr=curr.children[s[i]]

            if curr.isEnd:
                res=dfs(i+1,curr,word) or dfs(i+1,root,"")
            else:
                res=dfs(i+1,curr,word)
            dp[i,curr,word]=res
            return dp[i,curr,word]
        return dfs(0,root,"")