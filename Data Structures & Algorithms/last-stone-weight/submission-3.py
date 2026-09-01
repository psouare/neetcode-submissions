class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap=[0]*len(stones)

        for i,s in enumerate(stones):
            minheap[i]=-stones[i]
        heapq.heapify(minheap)

        while len(minheap)>1:
            x=-heapq.heappop(minheap)
            y=-heapq.heappop(minheap)

            if x==y:
                continue
            
            heapq.heappush(minheap,-abs(x-y))
        

        return -heapq.heappop(minheap) if minheap else 0
