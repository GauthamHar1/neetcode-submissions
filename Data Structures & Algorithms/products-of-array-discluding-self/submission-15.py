from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # now lets see if we can get the O(n) time 
        output = []
        left = nums
        right = list(reversed(nums))
        for i in range(1,len(left)):
            left[i] = left[i]*left[i-1]
        for i in range(1,len(right)):
            right[i] = right[i]*right[i-1]
        print(left)
        right = list(reversed(right))
        # now for each num excluded we just got the index before in left
        # and the index after in right, and multiply
        for i in range(len(nums)):
            if i==0:
                output.append(right[1])
            elif i==len(nums)-1:
                output.append(left[len(nums)-2])
            else:
                output.append(left[i-1]*right[i+1])
        return output
            

