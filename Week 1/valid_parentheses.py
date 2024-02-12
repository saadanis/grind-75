class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in pairs:
                if len(stack) > 0:
                    if not stack.pop() == pairs[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        else:
            return False