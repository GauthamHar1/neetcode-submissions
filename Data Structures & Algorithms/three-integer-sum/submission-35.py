from collections import defaultdict
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # so basically we go through nums, for each num run two pointers
        # to find two values that add up to -num
        result = []
        no_dups = set()
        for i in range(len(nums)):
            target = -nums[i]
            p1,p2 = 0,(len(nums)-1)
            while p2>p1:
                if p1==i:
                    p1+=1
                    continue
                if p2==i:
                    p2-=1
                    continue
                cur = nums[p1]+nums[p2]
                ls = [nums[i],nums[p1],nums[p2]]
                if cur==target and tuple(sorted(ls)) not in no_dups:
                    result.append(ls)
                    no_dups.add(tuple(sorted(ls)))
                elif cur<target:
                    p1+=1
                    
                else:
                    p2-=1
                    
        return result
                        





      


        
