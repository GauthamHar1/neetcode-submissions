from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the idea here is to start at every possible starting point
        # meaning there should be no n-1 in the set, and keep incrementing
        # by 1 until you find something not in set, do that for all the possible
        # starting points and then find which is the longest
        s = set(nums)
        longest = 0
        for num in s:
            if (num-1) not in s:
                length = 1
                while(num + length) in s:
                    length+=1
                longest = max(length,longest)
        return longest


