class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        memo = []
        for c in tokens:
            if c in ['+', '-', '*', '/']: 
                c = self.calculate(c, memo.pop(), memo.pop())
            memo.append(int(c))
        return memo[-1]
        
    def calculate(self, op, v1, v2):
        match op:
            case '+': return v2 + v1
            case '-': return v2 - v1
            case '*': return v2 * v1
            case '/': return v2 / v1