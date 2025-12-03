class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows-1

        while top<=bot:
            row_mid = (top+bot) // 2

            if target>matrix[row_mid][-1]:
                top = row_mid+1
            
            elif target < matrix[row_mid][0]:
                bot = row_mid-1
            
            else:
                break
        
        if not (top<=bot):
            return False
        
        l=0
        r=cols-1
        while l<=r:
            mid = (l+r)//2

            if target > matrix[row_mid][mid]:
                l = mid+1
            elif target < matrix[row_mid][mid]:
                r = mid-1
            else:
                return True
        return False
        