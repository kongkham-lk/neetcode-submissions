class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = ''.join(sorted(s1))
        for l in range(len(s2)):
            sorted_s2 = ''.join(sorted(s2[l:l+len(s1)]))
            if sorted_s1 == sorted_s2: return True

        return False