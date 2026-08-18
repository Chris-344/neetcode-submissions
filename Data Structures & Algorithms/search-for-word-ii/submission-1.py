class TrieNode:
    def __init__(self) -> None:
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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)

        ROW,COL=len(board),len(board[0])
        res,visited=[],set()

        def dfs(r,c,word,node):
            if (r<0 or c<0 or r==ROW or c==COL or board[r][c] not in node.children 
            or (r,c) in visited):
                return

            visited.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.isEnd:
                res.append(word)
                node.isEnd=False
            
            dfs(r+1,c,word,node)
            dfs(r-1,c,word,node)
            dfs(r,c+1,word,node)
            dfs(r,c-1,word,node)
            visited.remove((r,c))
        for i in range(ROW):
            for j in range(COL):
                if (i,j) not in visited:
                    dfs(i,j,"",root)
        return res