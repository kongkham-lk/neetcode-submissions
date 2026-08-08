class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 0: return 0

        freq = {}
        max_freq, l = 0, 0

        for r in range(len(s)):
            if s[r] not in freq: freq[s[r]] = 0
            freq[s[r]] += 1

            if (r - l + 1) - max(freq.values()) > k: 
                freq[s[l]] -= 1
                l += 1

            max_freq = max(max_freq, r-l+1)

        return max_freq
