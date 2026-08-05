class TrieNode:
    def __init__(self):
        self.isEndOfWord=False
        self.children={}

class WordDictionary:

    def __init__(self):
        self.node=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.node
        for i in word:
            if i not in curr.children:
                curr.children[i]=TrieNode()
            curr=curr.children[i]
        curr.isEndOfWord=True
    def search(self, word: str) -> bool:
        return self._search_recursive(self.node, word, 0)

    def _search_recursive(self, node, word: str, index: int) -> bool:
        # Base case: reached end of word
        if index == len(word):
            return node.isEndOfWord
        
        char = word[index]
        
        # If current character is a wildcard
        if char == ".":
            # Try all possible children
            for child in node.children.values():
                if self._search_recursive(child, word, index + 1):
                    return True
            return False
        
        # Normal character lookup
        if char not in node.children:
            return False
        
        return self._search_recursive(node.children[char], word, index + 1)