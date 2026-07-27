class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the area is (p1-p2)* min(heights[p1],heights[p2])
        # then lets move the one with lower height
        p1,p2 = 0,(len(heights)-1)
        area = 0
        while p2>p1:
            if heights[p1]<=heights[p2]:
                cur_area = (p2-p1)*heights[p1]
                area = max(cur_area,area)
                p1+=1
            else:
                cur_area = (p2-p1)*heights[p2]
                area = max(cur_area,area)
                p2-=1
        return area

