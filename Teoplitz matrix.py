class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """ 
    # we know that we need to check the (i+1 , j+1) and the (i , j)

        colNums = len(matrix[0]) - 1
        rowNums = len(matrix) - 1

        for i in range(rowNums):
            for j in range(colNums):
                if(matrix[i][j]!=matrix[i+1][j+1]):
                    return False
        return True
