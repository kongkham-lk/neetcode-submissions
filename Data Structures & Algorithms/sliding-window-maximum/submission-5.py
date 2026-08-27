import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # run check max val in this current window -> get max_idx
        # compare the curr max and new el -> get new max_idx
        # check if max_idx in window,
            # if yes -> add
            # find new max_idx, then add

        max_val = max(nums[0:k])
        res = []

        for l in range(len(nums)-k+1):
            r = l + k - 1
            if max_val == nums[l-1]: max_val = max(nums[l:r+1])
            elif max_val < nums[r]: max_val = nums[r]
            res.append(max_val)
        return res


