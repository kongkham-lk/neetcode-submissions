class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_temp, t_temp = [0]*26, [0]*26
        for i in range(len(s)): 
            s_temp[ord(s[i])-97] += 1
            t_temp[ord(t[i])-97] += 1
        return "".join(map(str, s_temp)) == "".join(map(str, t_temp))