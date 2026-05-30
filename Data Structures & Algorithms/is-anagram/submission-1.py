class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_temp, t_temp = [0]*26, [0]*26
        for c in s: s_temp[ord(c)-97] += 1
        for c in t: t_temp[ord(c)-97] += 1
        return "".join(map(str, s_temp)) == "".join(map(str, t_temp))