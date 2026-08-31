class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        mid = r
        res = float("inf")
        while l <= r and mid != 0:
            print(l, r, mid)
            if self.can_finish(piles, h, mid): 
                res = min(res, mid)
                r = mid-1
            else: 
                l = mid + 1
            mid = (r - l)//2 + l
        return res
        
    def can_finish(self, piles, h, k):
        spent_hour = 0
        for b in piles: 
            spent_hour += math.ceil(b / k)
        return True if spent_hour <= h else False
