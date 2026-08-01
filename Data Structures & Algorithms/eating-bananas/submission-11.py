class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ok so the max bananas per hour is the max elem in the list
        #  so if we have a list from 0 to max and do binary search
        # check 
        
        answer = -1
        l,r = 1,max(piles)+1
        
        while l<r:
            mid = l+((r-l)//2)
            hours = 0
            for pile in piles:
                if pile%mid==0:
                    hours+=pile//mid
                else:
                    hours+=(pile//mid)+1
            if hours>h:
                l = mid+1   
            else:
                answer = mid
                r = mid
        return answer

