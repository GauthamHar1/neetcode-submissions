class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if nums[mid]<nums[r]:
        #   this means the lower part of the array is from mid
        # or below mid up to r, so we have to check if target 
        # greater than nums[mid] and less than equal to nums[r] then we take the right chunk
        # if target is less than nums[mid] then we know that its
        # in the left chunk
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l+((r-l)//2)
            if nums[mid]==target:
                return mid
            if nums[l]<nums[r]:
                if nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]>nums[r]:
                    if target>nums[mid] or target<=nums[r]:
                        l = mid+1
                    elif target<nums[mid] and target>nums[r]:
                        r = mid-1
                else:
                    if target > nums[mid] and target<=nums[r]:
                        l = mid+1
                    elif target < nums[mid] or target>nums[r]:
                        r = mid-1
        return -1


