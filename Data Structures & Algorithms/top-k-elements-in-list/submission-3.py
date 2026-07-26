from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num]+=1
        heap = []
        # the idea is to use a min heap
        for key,val in list(hm.items()):
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        # now we just have the top k ones in the min heap
        return list(map((lambda a:a[1]),heap))
            


