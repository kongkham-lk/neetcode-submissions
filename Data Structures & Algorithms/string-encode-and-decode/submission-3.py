class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1: return ''
        res = ''
        for s in strs: res += str(len(s))+','
        res += '||'
        for s in strs: res += s
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) < 1: return []
        temp = s.split('||')
        print(temp)
        length, text = list(map(int, temp[0][:-1].split(','))), temp[1]
        res, i = [], 0
        for l in length:
            res.append(text[i:i+l])
            i += l
        return res