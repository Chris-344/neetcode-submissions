class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj=defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern= word[:j] + "*" +word[j+1:]
                adj[pattern].append(word)
        
        que=collections.deque()
        visit=set()
        visit.add(beginWord)
        res=1
        que.append(beginWord)

        while que:
            for _ in range(len(que)):
                cur=que.popleft()
                if cur==endWord:
                    return res
                for j in range(len(cur)):
                    pattern=cur[:j]+"*"+cur[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            que.append(nei)
            res+=1
        return 0