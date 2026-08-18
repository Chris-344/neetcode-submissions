class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
        curr.isEndOfWord=True

    def search(self, word: str) -> bool:
        def dfs(j,node):
            curr=node
            for i in range(j,len(word)):
                    c=word[i]
                    if c==".":
                        for ch in curr.children.values():
                            if dfs(i+1,ch):
                                return True
                        return False
                    else:
                        if c not in curr.children:
                            return False
                        curr=curr.children[c]
            return curr.isEndOfWord
        return dfs(0,self.root)





