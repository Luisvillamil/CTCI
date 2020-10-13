# 1-8 Zero Matrix
# leetcode problem: https://leetcode.com/problems/set-matrix-zeroes/

# O(m+n) space solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        columns = {}
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for column in range(n):
                if matrix[row][column] == 0:
                    if row not in rows:
                        rows[row] = 1
                    if column not in columns:
                        columns[column] = 1
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in columns:
            for i in range(m):
                matrix[i][j] = 0
        return
                    
        """
        Do not return anything, modify matrix in-place instead.
        """
        

# O(1) space solution
class Solution:
    def nullcol(self,matrix,col):
        for i in range(0,len(matrix)):
            matrix[i][col] = 0
    def nullrow(self,matrix,row):
        for j in range(0,len(matrix[0])):
            matrix[row][j] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zerorow = False
        zerocol = False
        for j in range(n):
            if matrix[0][j] == 0:
                zerorow = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                zerocol = True
                break
        for row in range(1,m):
            for column in range(1,n):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                self.nullrow(matrix,i)
        for j in range(1,n):
            if matrix[0][j] == 0:
                self.nullcol(matrix,j)
        if zerorow:
            self.nullrow(matrix,0)
        if zerocol:
            self.nullcol(matrix,0)
        return

