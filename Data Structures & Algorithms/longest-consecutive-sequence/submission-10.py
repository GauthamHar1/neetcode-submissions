class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # can't sort because must be O(n)
        # what if we first make a set of the elements for O(1) lookup
        # then go through the array and for each element keep adding 1
        # and checking set until not found and keep track of current max

        longest = 0
        check = set(nums)
        for num in nums:
            length = 0
            local_num = num
            while True:
                if local_num in check:
                    length+=1
                    local_num+=1
                else:
                    break
            longest = max(length,longest)
        return longest
