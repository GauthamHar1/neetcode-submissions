class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(logn)
        cars = sorted(zip(position,speed))
        stack = []
        # we need to compare the time at dest for each elem
        # t_dest = (target - elem[0])/elem[1]
        # if t_dest of something at a farther position is greater
        # than t_dest of something at a closer position then 
        for p,s in cars[::-1]:
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)





