class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = []
        a, b = 0, 0

        while a < len(nums1) and b < len(nums2):
            if nums1[a] <= nums2[b]:
                merge_list.append(nums1[a])
                a+=1
            else:
                merge_list.append(nums2[b])
                b+=1
                
        for i in range(a, len(nums1)): merge_list.append(nums1[i])
        for i in range(b, len(nums2)): merge_list.append(nums2[i])

        size = len(merge_list)
        # print(merge_list, size//2)
        if size % 2 == 1: return merge_list[size//2]
        else: return (merge_list[(size//2)-1] + merge_list[size//2]) / 2
