class Solution:
    def trap(self, height: List[int]) -> int:
        # ok lets try to implement the solution
        total_water = 0
        l,r = 0,(len(height)-1)
        Lmax,Rmax = height[l],height[r]
        while l<r:
            if Lmax<=Rmax:
                l+=1
                total_water+=max(0,Lmax-height[l])
                Lmax = max(Lmax,height[l])
            else:
                r-=1
                total_water+=max(0,Rmax-height[r])
                Rmax = max(Rmax,height[r])
        return total_water

          
