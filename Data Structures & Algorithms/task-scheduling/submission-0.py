class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-frequency for frequency in count.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)

                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush(heap, cnt)

        return time
        