class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        daHeap=[-cnt for cnt in count.values()]
        heapq.heapify(daHeap)
        time=0
        q=deque()


        while daHeap or q:
            time+=1

            if not daHeap:
                c,time=q[0]
            else:
                cnt=1+heapq.heappop(daHeap)
              
                if cnt:
                    q.append([cnt,time+n]) 
            if q:
                    c,qt=q[0]

                    if qt==time:
                        heapq.heappush(daHeap,c)
                        q.popleft()

        return time





    