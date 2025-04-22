import heapq

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def delete(self):
        if self.heap:
            return heapq.heappop(self.heap)

    def traverse(self):
        for item in self.heap:
            pass
