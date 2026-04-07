class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix), len(matrix[0])
        top_r,bot_r = 0, row-1
        while top_r<=bot_r:
            row_mid = (top_r+bot_r)//2
            if target > matrix[row_mid][-1]:
                top_r = row_mid+1
            elif target < matrix[row_mid][0]:
                bot_r = row_mid-1
            else:
                break
        if not (top_r <= bot_r):
            return False
        row = (top_r+bot_r)//2
        l,r = 0,col-1
        while l<=r:
            mid = (l+r)//2
            if target < matrix[row][mid]:
                r = mid-1
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                return True
        return False


        
        