class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tkn in tokens:
            if (tkn == "+"):
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i1 + i2)
            elif (tkn == "-"):
                i2 = stack.pop()
                i1 = stack.pop()
                stack.append(i1 - i2)
            elif (tkn == "*"):
                i1 = stack.pop()
                i2 = stack.pop()
                stack.append(i1 * i2)
            elif (tkn == "/"):
                i2 = stack.pop()
                i1 = stack.pop()
                stack.append(int(i1 / i2))
            else:  
                stack.append(int(tkn));
        
        return int(stack.pop())