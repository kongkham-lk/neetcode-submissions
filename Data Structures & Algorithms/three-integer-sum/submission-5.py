class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp_set = set()
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0: 
                    temp_set.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0: l += 1
                else: r -= 1
        return [list(l) for l in temp_set]
