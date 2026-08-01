class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        q = [] 
        temp = Counter(tasks)
        freq = [-cnt for cnt in temp.values()]
        heapq.heapify(freq)

        while q or freq:
            time += 1
            if freq:
                curr = heapq.heappop(freq) + 1  
                if curr:
                    q.append([curr, time + n])

            if q and q[0][1] == time:
                heapq.heappush(freq, q.pop(0)[0])

        return time