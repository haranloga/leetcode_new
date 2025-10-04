class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapParenthesis = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # If c is a closing bracket, check top of stack
            if c in mapParenthesis:
                if stack and stack[-1] == mapParenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                # c is an opening bracket; push to stack
                stack.append(c)

        # Valid only if nothing left unmatched on the stack
        return not stack
