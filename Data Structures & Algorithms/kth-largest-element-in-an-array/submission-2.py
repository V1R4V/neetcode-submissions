class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap approach
        # nums = [-i for i in nums]
        # n=1
        # heapq.heapify(nums)
        # while n<k:
        #     heapq.heappop(nums)
        #     n+=1
        # return -(heapq.heappop(nums))

        #min heap approach 
        heap=[]
        heapq.heapify(heap)
        for i in nums:
            heapq.heappush(heap,i)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]



        