class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_l, max_r = 0, 0
        res = 0

        while l <= r:
            if max_l <= max_r:
                temp = max_l - height[l]
                res += temp if temp > 0 else 0
                max_l = max(max_l, height[l])
                l += 1
            else:
                temp = max_r - height[r]
                res += temp if temp > 0 else 0
                max_r = max(max_r, height[r])
                r -= 1

        return res