class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initial thoughts
        # push on to stack if an operator comes up, then pop two things
        # perform the operation, then push the result back on to the stack
        stack = []
        for tok in tokens:
            print(stack)
            match tok:
                case "*":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a*b)
                    
                case "+":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a+b)
                case "-":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b-a)
                case "/":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b/a)
                case _:
                    stack.append(tok)

        return int(stack[-1])