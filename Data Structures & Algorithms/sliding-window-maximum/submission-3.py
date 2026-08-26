class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # run check max val in this current window -> get max_idx
        # compare the curr max and new el -> get new max_idx
        # check if max_idx in window,
            # if yes -> add
            # find new max_idx, then add

        # max_val, max_idx = self.find_max_val(nums, 0, k)
        max_val = max(nums[0:k])
        res = []
        # print(res)

        for l in range(len(nums)-k+1):
            r = l + k - 1
            # if max_val < nums[r]:
            #     max_val = nums[r]
                # max_idx = r
            if max_val == nums[l-1]:
                max_val = max(nums[l:r+1])
                # print(" >>> find new max:", max_val, ", from:", nums[l:r+1])
            elif max_val < nums[r]:
                max_val = nums[r]
                # print(" >>> compare with new el:", max_val, nums[r])
            res.append(max_val)
            # print(l, r, nums[r], nums[l:r+1], res)
        return res


    # def find_max_val(self, nums, l, k):
    #     max_val, max_idx = float('-inf'), -1
    #     for i in range(l, l+k):
    #         if max_val < nums[i]:
    #             max_val = nums[i]
    #             max_idx = i
    #     return max_val, max_idx