# 1-7 Rotate Matrix 
# Similar code in leetcode: https://leetcode.com/problems/rotate-image/submissions/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for layer in range(len(matrix)//2):
            first = layer
            last = len(matrix) - layer - 1
            for i in range(first,last):
                offset = i - first
                temp = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = temp
                
        """
        Do not return anything, modify matrix in-place instead.
        """
