class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # tar_row_idx = self.search_row(matrix, target)
        # res = self.search_col(matrix, target, tar_row_idx) 
        # return True if res != -1 else False
        return True if self.search_col(matrix, target, self.search_row(matrix, target)) != -1 else False

    def search_row(self, matrix: List[List[int]], target: int) -> int:
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (r-l)//2+l
            # print("mid row:",mid, l, r)
            if target in matrix[mid]: return mid
            elif target < matrix[mid][0]: r = mid-1
            else: l = mid+1
        return -1

    def search_col(self, matrix: List[List[int]], target: int, tar_row_idx: int) -> int:
        if tar_row_idx == -1: return -1

        tar_row = matrix[tar_row_idx]
        l, r = 0, len(tar_row)-1
        # print(tar_row)
        while l <= r:
            mid = (r-l)//2+l
            # print("mid col:",mid, l, r)
            if target == tar_row[mid]: return mid
            elif target < tar_row[mid]: r = mid-1
            else: l = mid+1
        return -1