class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 0: return 0

        memo = {}
        res, l, r = 0, 0, 0

        while r < len(s):
            if s[r] not in memo: memo[s[r]] = 0
            memo[s[r]] += 1

            count = (r - l + 1) - max(memo.values()) if memo else 0

            if count > k: 
                memo[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
            r += 1

        return res
