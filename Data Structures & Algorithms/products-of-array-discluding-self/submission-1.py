class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for n in nums:
            if n == 0: zero_count += 1
            else: prod *= n

        if zero_count > 1: return [0]*len(nums)

        res = []
        for n in nums:
            if zero_count > 0: res.append(0 if n != 0 else prod)
            else: res.append(prod // n)
        return res