class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the idea here, is basically we want to sort the array an
        cars = sorted(zip(position,speed))
        # for the stack we basically wanna think of it as candy crush kinda,
        # like go from right to left putting the highest position lower on the stack
        # and if something at a lower position gets put but its time is greater
        # then you pop(), or acc, couldn't you just not put it
        stack = []
        for p,s in cars[::-1]:
            t  = (target-p)/s
            if not stack:
                stack.append(t)
            elif stack[-1]>=t:
                continue
            else:
                stack.append(t)
        return len(stack)
            