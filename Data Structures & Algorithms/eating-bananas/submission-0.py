class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l < r:
            temp_res = 0
            speed = (l+r) // 2
            for p in piles: 
                temp_res += math.ceil(p / speed)
                if temp_res > h: break
            if temp_res > h: l = speed+1
            else: res = r = speed
        return res
        