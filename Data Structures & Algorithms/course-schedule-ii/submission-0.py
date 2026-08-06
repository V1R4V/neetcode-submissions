class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adj list
        adj = [[] for i in range(numCourses)]
        indegree = [0]*numCourses #this will track indegree or the courses we can get started with 
        ans=[]
        #create the adj or graph 
        for cor,pre in prerequisites:
            adj[pre].append(cor)
            indegree[cor]+=1
        q=deque()

        for cor in range(numCourses): #cycle detection happens here 
            if indegree[cor]==0:
                q.append(cor)
        while q:
            cor = q.popleft()

            for nei in adj[cor]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
            ans.append(cor)
        return ans if len(ans)==numCourses else []



        
        

        

        