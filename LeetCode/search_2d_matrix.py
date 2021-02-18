class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_boundary = len(matrix[0])
        col_index = 0
        
        while col_index < len(matrix):
            
            for i in range(row_boundary):
                if matrix[col_index][i] == target:
                    return True
                elif matrix[col_index][i] > target:
                    if i == 0:
                        return False
                    else:
                        row_boundary = i
                        break
            
            col_index += 1
        else:
            return False