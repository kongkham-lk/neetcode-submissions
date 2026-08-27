class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_symbol = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }
        
        for c in s:
            # print(c)
            if c in open_symbol: stack.append(open_symbol[c])
            else:
                if not stack: return False
                temp = stack.pop()
                # print("temp:", temp)
                if c != temp: return False
        return True if not stack else False

        