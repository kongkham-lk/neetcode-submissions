class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)] # if do [[]]*26 -> create same ref of [] 26 element
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, val in count.items():
            arr[val].append(key)

        for i in range(len(arr)-1,-1,-1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k: return res
        return res