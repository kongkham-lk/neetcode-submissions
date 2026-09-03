class Solution:
    def search(self, nums: List[int], tar: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if tar == nums[mid]: return mid
            elif nums[l] <= nums[mid]:
                if tar >= nums[l] and tar <= nums[mid]: r = mid-1
                else: l = mid+1
            else:
                if tar >= nums[mid] and tar <= nums[r]: l = mid+1
                else: r = mid-1
        return -1