class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "]": "[", "}": "{"}
        
        for p in s:
            if p in parentheses.values():
                stack.append(p)
            elif p in parentheses.keys():
                # Check if stack is empty or top element doesn't match
                if not stack or stack.pop() != parentheses[p]:
                    return False
                    
        return len(stack) == 0
