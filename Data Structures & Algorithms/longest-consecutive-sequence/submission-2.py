class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        sort_nums = list(sorted(nums))
        print(sort_nums)
        res, count, prev = 0, 1, sort_nums[0]
        for i in range(1,len(nums)):
            if sort_nums[i] == prev: continue
            if sort_nums[i] == prev+1: count += 1
            else: 
                res = max(res,count)
                count = 1
            prev = sort_nums[i]
        return max(res,count)