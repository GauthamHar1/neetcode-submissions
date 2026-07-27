from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # lets rethink, i misunderstood the problem, they don't
        # have to appear in consecutive order in the original array

        # my idea is to essentially build out the hashmap with different
        # consecutive lists, then at the end try to merge them together

        s = set(nums)
        longest = 0
        for num in s:
            if (num-1) not in s:
                length = 1
                while(num + length) in s:
                    length+=1
                longest = max(length,longest)
        return longest
        # now for each num in nums, keep checking if num+1 is 


