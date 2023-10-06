class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        matrix = [[0] * 101 for i in range(101)]
        matrix[0][0] = poured

        for i in range(1, 101):
            for j in range(i + 1):
                if j == 0:
                    matrix[i][j] = max((matrix[i - 1][j] - 1) / 2, 0)
                elif j == i:
                    matrix[i][j] = max((matrix[i - 1][j - 1] - 1) / 2, 0)
                else:
                    matrix[i][j] = max((matrix[i - 1][j - 1] - 1) / 2, 0) + max((matrix[i - 1][j] - 1) / 2, 0)
                if matrix[i][j] != 0:
                    print("matrix[%s][%s] = %s" % (i, j, matrix[i][j]))
        return min(matrix[query_row][query_glass], 1.0)
        

solution = Solution()
#ret = solution.champagneTower(1, 1, 1)
#ret = solution.champagneTower(2, 1, 1)
#ret = solution.champagneTower(100000009, 33, 17)
ret = solution.champagneTower(25, 6, 1)
print(ret)