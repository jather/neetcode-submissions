class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b, t = 0, len(matrix) - 1
        m = None
        while b <= t:
            m = (b + t) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            if target < matrix[m][0]:
                t = m - 1
            else:
                b = m + 1
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            c = (l + r) // 2
            if matrix[m][c] == target:
                return True
            if target < matrix[m][c]:
                r = c - 1
            else:
                l = c + 1
        return False