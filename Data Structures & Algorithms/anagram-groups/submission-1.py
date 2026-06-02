class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            t = [0]*26
            for c in s:
                t[ord(c)-97]+=1
            key = ",".join(map(str, t))
            print(key, s)
            if key in res: res[key].append(s)
            else: res[key] = [s]
        return list(res.values())