class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # O(logn)
        cars = sorted(zip(position,speed))
        stack = []
        
        for p,s in cars[::-1]:  
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)





