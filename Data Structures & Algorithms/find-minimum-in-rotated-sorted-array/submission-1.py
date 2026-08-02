class Solution:
    def findMin(self, nums: List[int]) -> int:
        # im thinking we run binary search looking for the point
        # where nums[i]<nums[i-1] and then we should return nums[i]
        # and if that point isn't found then we return nums[0] 
        # as that means the array was returned back to its original 
        # state
        l,r = 0,len(nums)-1
        if nums[l]<=nums[r]:
            return nums[l]
        while l<r:
            mid = l+((r-l)//2)
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[mid]<nums[r]:
                r = mid
            else:
                l = mid + 1
            
        return -1

        
        