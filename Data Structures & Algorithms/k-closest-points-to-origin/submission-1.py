import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dpoint=[]
        for i, point in enumerate(points):
            heapq.heappush(dpoint,(math.dist(point,(0,0)),i))
        
        result=[]
        while k>0:
            if dpoint:
                result.append(points[heapq.heappop(dpoint)[1]])
            k-=1

        return result

            