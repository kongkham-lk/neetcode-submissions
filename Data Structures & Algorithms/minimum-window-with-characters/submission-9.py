class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t

        count_t, count_s = {}, {}
        for c in t: count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)
        res, resLen = "", float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            count_s[c] = count_s.get(c, 0) + 1

            if c in count_t and count_s[c] == count_t[c]: 
                have += 1
            
            while have == need:
                if (r-l+1) < resLen: 
                    res = s[l:r+1]
                    resLen = r-l+1
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]: 
                    have -= 1
                l+=1
        return res if resLen != float('inf') else ""
