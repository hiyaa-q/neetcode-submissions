class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        for c in s:
            if (c == '(' or c == '{' or c == '['):
                openStack.append(c)
            else:
                if not openStack: return False
                thisOpen = openStack.pop()
                if (c == ')' and thisOpen != '(') or (c == '}' and thisOpen != '{') or (c == ']' and thisOpen != '['): return False

        return (not openStack)
        