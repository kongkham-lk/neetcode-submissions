class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        memo = deque()
        for c in s:
            while c in memo:
                memo.popleft()
            memo.append(c)
            res = max(res, len(memo))
            # print(c, memo, res)
        return res