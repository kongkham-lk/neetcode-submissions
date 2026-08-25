class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        l_s1, l_s2 = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(s1)): 
            l_s1[ord(s1[i])-ord('a')] += 1
            l_s2[ord(s2[i])-ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if l_s1 == l_s2: return True
            l_s2[ord(s2[i-len(s1)])-ord('a')] -= 1
            l_s2[ord(s2[i])-ord('a')] += 1
            # print(s2[i-1], s2[i], "\n", l_s1, "\n", l_s2, "\n")
        if l_s1 == l_s2: return True
        return False

        # # # OPTION 1 -> Use sort then match the 2 sorted string
        # # sorted_s1 = ''.join(sorted(s1))
        # # for l in range(len(s2)):
        # #     sorted_s2 = ''.join(sorted(s2[l:l+len(s1)]))
        # #     if sorted_s1 == sorted_s2: return True

        # # return False

        # # # OPTION 2 -> Check for both exist and not exist char in s1 and s2
        # s1_count, s2_count = [0]*26, [0]*26
        # for i in range(len(s1)):
        #     s1_count[ord(s1[i])-ord('a')] += 1
        #     s2_count[ord(s2[i])-ord('a')] += 1
        
        # matches = sum(s1_count[i] == s2_count[i] for i in range(26))

        # for r in range(len(s1), len(s2)):
        #     l = r-len(s1)
        #     if matches == 26: return True

        #     i_l, i_r = ord(s2[l])-ord('a'), ord(s2[r])-ord('a')
        #     s2_count[i_l] -= 1
        #     s2_count[i_r] += 1
        #     if s1_count[i_l] == s2_count[i_l]: matches += 1
        #     else: matches -= 1
        #     if s1_count[i_r] == s2_count[i_r]: matches += 1
        #     else: matches -= 1
        
        # return matches == 26
        
