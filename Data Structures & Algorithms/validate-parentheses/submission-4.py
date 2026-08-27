class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_symbol = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }
        
        for c in s:
            if c in open_symbol: stack.append(open_symbol[c])
            elif not stack or c != stack.pop(): return False
        return True if not stack else False

        