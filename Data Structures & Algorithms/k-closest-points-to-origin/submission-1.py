class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # originx,originy=0,0
        # sort=sorted(points,key=lambda points: (points[0]**2 + points[1]**2))
        # return sort[:k]
        heap=[]
        heapq.heapify(heap)
        for i in points:
            x,y=i[0],i[1]
            distance= x**2 + y**2
            heapq.heappush(heap,(distance,x,y))
        res=[]
        for i in range(k):
            point = heapq.heappop(heap)
            res.append([point[1],point[2]])
        return res