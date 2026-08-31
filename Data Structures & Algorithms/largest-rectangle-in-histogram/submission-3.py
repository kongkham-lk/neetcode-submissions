class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        # size = len(heights)
        # for i in range(size):
        #     left_count, right_count = 0, 0
        #     for l in range(i-1, -1, -1):
        #         if heights[l] >= heights[i]: left_count += heights[i]
        #         else: break
        #     for r in range(i+1, size, +1):
        #         if heights[r] >= heights[i]: right_count += heights[i]
        #         else: break
        #     res = max(res, heights[i] + left_count + right_count)
        # return max(res, max(heights))

        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        heights.pop()
        return res

    