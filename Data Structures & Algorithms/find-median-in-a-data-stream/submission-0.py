import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max-heap (negated)
        self.right = []  # min-heap

    def addNum(self, num: int) -> None:
        A, B = len(self.left), len(self.right)

        if not self.left:
            heapq.heappush(self.left, -num)
            return

        leftMax = -self.left[0]
        rightMin = self.right[0] if self.right else leftMax

        if num < leftMax and A <= B:
            heapq.heappush(self.left, -num)
        elif num < leftMax and A > B:
            curr = -heapq.heappop(self.left)
            heapq.heappush(self.left, -num)
            heapq.heappush(self.right, curr)
        elif num >= rightMin and A >= B:
            heapq.heappush(self.right, num)
        elif num >= rightMin and A < B:
            curr = heapq.heappop(self.right)
            heapq.heappush(self.right, num)
            heapq.heappush(self.left, -curr)
        else:
            if A > B:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)

    def findMedian(self) -> float:
        A, B = len(self.left), len(self.right)
        if (A + B) % 2:
            return -self.left[0] if A > B else self.right[0]
        return (-self.left[0] + self.right[0]) / 2
        