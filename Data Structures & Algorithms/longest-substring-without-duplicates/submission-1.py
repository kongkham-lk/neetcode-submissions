class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, memo = 0, deque()
        for c in s:
            while c in memo: memo.popleft()
            memo.append(c)
            res = max(res, len(memo))
        return res