class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq=defaultdict(list)
        for cor,pre in prerequisites:
            prereq[cor].append(pre)
        visit = set()

        def dfs(cor):
            if cor in visit:
                return False
            if prereq[cor]==[]:
                return True
            visit.add(cor)
            for pre in prereq[cor]:
                if not dfs(pre): return False
            visit.remove(cor)
            prereq[cor]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True