class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # One thing i can think of is a two pointer approach, essentially
        # have one ptr that goes through each elem, then for each elem
        # the other pointer goes ahead until it finds a temp greater
        # then it adds result[p1] = p2-p1 this would be O(n^2) worst case
        # n(n+1)/2, best case it could be O(n) if the temps are in dec
        # order

        # we keep a stack that has the current max
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            print(stack)
            print(result)
            if stack:
                if stack[-1][0]>=temperatures[i]:
                    stack.append((temperatures[i],i))
                else:
                    while stack and stack[-1][0]<temperatures[i]:
                        elem = stack.pop()
                        result[elem[1]] = i-elem[1]
                    stack.append((temperatures[i],i))
            else:
                stack.append((temperatures[i],i))
        return result

