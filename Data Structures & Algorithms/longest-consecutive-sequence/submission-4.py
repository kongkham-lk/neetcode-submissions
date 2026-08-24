class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sort_nums = sorted(nums)
        res = [1 for _ in range(len(nums))]

        for i in range(len(sort_nums)-2, -1, -1):
            if sort_nums[i] + 1 == sort_nums[i+1]: res[i] += res[i+1]
            elif sort_nums[i] == sort_nums[i+1]: res[i] = res[i+1]
            
        return max(res) if res else 0
