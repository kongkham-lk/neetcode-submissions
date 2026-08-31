class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        mid = r
        res = float("inf")
        while l <= r:
            print(l, r, mid)
            if self.can_finish(piles, h, mid): 
                # print("-> valid:", mid)
                res = min(res, mid)
                r = mid-1
            else: 
                # print("-> not valid:", mid)
                l = mid + 1
            mid = (r - l)//2 + l
            if mid == 0: break
        return res
        
    def can_finish(self, piles, h, k):
        spent_hour = 0
        for b in piles: 
            spent_hour += math.ceil(b / k)
        #     print("     spent_hour:", b/k, "=", b, k)
        # print("   Check:", spent_hour, h)
        return True if spent_hour <= h else False
