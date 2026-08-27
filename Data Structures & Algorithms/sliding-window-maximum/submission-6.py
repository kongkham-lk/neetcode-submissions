import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # Approach 1 - sliding window - consistently compare el if max_val in the range, else get the next max_val
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

        # # Approach 2 - use max heap -> for each range, pop all till the last one then add to res
        res = []
        heap_max = []

        for l in range(len(nums)):
            heapq.heappush(heap_max, (-num[i], i))
            if i >= k-1:
                while heap_max[0][1] <= i-k:
                    heapq.heappush(heap_max)
                res.append(max_heap[0][0])
        return res