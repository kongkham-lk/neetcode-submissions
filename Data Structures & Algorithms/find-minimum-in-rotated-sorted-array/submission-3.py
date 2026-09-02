class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            # print(l, mid, r)
            res = min(res, nums[mid])
            if nums[l] > nums[mid]: r = mid-1
            else: l = mid+1
        return res




        # # this is for finding the number of rotation apply on the sorted array
        # if nums[0] < nums[-1]: return 0

        # l, r = 0, len(nums)-1
        # tar = min(nums)

        # while l <= r:
        #     mid = ((r-l)//2+l)%len(nums)
        #     if tar == nums[mid]: return mid
        #     elif tar < nums[mid] and tar > nums[l]: r = (mid-1)%len(nums)
        #     else: l = (mid+1)%len(nums)
        