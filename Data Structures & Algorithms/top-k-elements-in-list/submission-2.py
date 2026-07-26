from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        hm = defaultdict(int)
        for num in nums:
            hm[num]+=1
        # so now we have a frequency table
        # we need to get the keys with the
        # top k values first to get the top k
        # values we could get the max of the values
        # k times, removing the max found each time
        # then to get the keys associated, since any
        # order is fine we can just use .keys() and
        # append any with the correct value to the output
        topk = []
        counts = list(hm.values())
        for _ in range(k):
            topk.append(max(counts))
            counts.remove(max(counts))
        for elem in topk:
            for key in list(hm.keys()):
                if hm[key] == elem and key not in output:
                    output.append(key) 
        return output

        