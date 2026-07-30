class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        Lmax,Rmax=height[l],height[r]
        total = 0
        while l<r:           
            if Lmax <= Rmax:
                total+=Lmax-height[l]
                l+=1
                Lmax = max(Lmax,height[l])
            else:
                total+=Rmax-height[r]
                r-=1
                Rmax = max(Rmax,height[r])    
        return total

            