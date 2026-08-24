class Solution:
    def trap(self, h: List[int]) -> int:
        l, r = 0, len(h)-1
        max_l, max_r = 0, 0
        res = 0

        while l <= r: # need to include the mid col as well (where l == r)
            if max_l <= max_r:
                temp = max_l - h[l]
                res += temp if temp > 0 else 0
                max_l = max(max_l, h[l])
                l += 1
            else:
                temp = max_r - h[r]
                res += temp if temp > 0 else 0
                max_r = max(max_r, h[r])
                r -= 1
        return res