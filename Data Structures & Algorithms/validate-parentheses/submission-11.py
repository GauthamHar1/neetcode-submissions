class Solution:
    def isValid(self, s: str) -> bool:
        hm = {')':'(','}':'{',']':'['}
        stack = []
        # idea is have a stack and if its an opening one,
        # then add to the stack and if its a closing one, 
        # then check if the top of the stack matches it using
        # the lookup table (hm[closing]==top of stack?)
        # then if it does, pop, otherwise return false, check
        # that stack is empty at end
        for c in s:
            # if the next one in the string is 
            if c not in hm:
                stack.append(c)
            elif stack:
                if hm[c]!=stack.pop():
                    return False
            else:
                return False
        return len(stack)==0
                    

            
            