class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Flag to track if the FIRST ROW needs to be zeroed out
        rowZero = False

        # ---------------------------------------------------------
        # 1) FIRST PASS:
        # Use first row and first column as markers.
        # If matrix[r][c] == 0:
        #    mark matrix[r][0] = 0  → mark entire row r
        #    mark matrix[0][c] = 0  → mark entire column c
        # ---------------------------------------------------------
        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == 0:

                    # Mark the column
                    matrix[0][c] = 0

                    # Mark the row
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        # If zero is in FIRST ROW, remember this
                        rowZero = True

        # ---------------------------------------------------------
        # 2) SECOND PASS:
        # Use the markers to set cells to zero.
        # (Skip first row & first column for now)
        # ---------------------------------------------------------
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # ---------------------------------------------------------
        # 3) HANDLE FIRST COLUMN:
        # If matrix[0][0] is 0, it means **first column** must be zero
        # ---------------------------------------------------------
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # ---------------------------------------------------------
        # 4) HANDLE FIRST ROW:
        # If rowZero flag is True, zero out entire first row
        # ---------------------------------------------------------
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
