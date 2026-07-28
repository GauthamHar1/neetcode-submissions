from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ok so we can do a two pointer approach here
        # essentially, we have the equation -nums[i] = nums[j]+nums[k]
        # so we just make i go through the array and then run two sum
        # with that as the target
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            hm = defaultdict(int)
            for j in range(len(nums)):
                if j==i:
                    continue
                if target-nums[j] in hm and sorted([nums[i],nums[j],target-nums[j]]) not in result:
                    result.append(sorted([nums[i],nums[j],target-nums[j]]))
                hm[nums[j]] = j
        return result


            