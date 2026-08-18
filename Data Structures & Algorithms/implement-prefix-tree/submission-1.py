class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.isEndOfWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=TrieNode()
            curr=curr.children[i]
        curr.isEndOfWord=True

    def search(self, word: str) -> bool:
        curr=self.root
        i=0
        while curr and i<len(word):
            if word[i] in curr.children:
                curr=curr.children[word[i]]
                i+=1
            else:
                return False
        return curr.isEndOfWord 

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        i=0
        while curr and i<len(prefix):
            if prefix[i] in curr.children:
                curr=curr.children[prefix[i]]
                i+=1
            else:
                return False
        return True
