class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = []
        for i in range(len(nums)):
            if nums[i] in memo:
                for j in range(len(memo)):
                    if nums[i] == memo[j]: return [j, i]
            memo.append(target - nums[i])
        return []