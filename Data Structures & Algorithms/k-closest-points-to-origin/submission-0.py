class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result1=[]
        result2=[]

        for point in points:
            dist=point[0]**2+point[1]**2
            result1.append([dist,point[0],point[1]])

        heapq.heapify(result1)

        while k>0:
            dist,x,y=heapq.heappop(result1)
            result2.append([x,y])
            k-=1

        return result2








