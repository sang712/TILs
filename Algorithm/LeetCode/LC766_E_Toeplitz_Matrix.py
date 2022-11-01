'''
1행과 1열을 for문으로 돌고 대각선으로 움직이면서 같은 수로 되어있는지 확인하도록 구현하였음
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        delta = (1, 1)
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(n):
            r, c = 0, i
            start = matrix[r][c]
            while r < m and c < n:
                if start != matrix[r][c]:
                    return False
                r += delta[0]
                c += delta[1]
        for j in range(1, m):
            r, c = j, 0
            start = matrix[r][c]
            while r < m and c < n:
                if start != matrix[r][c]:
                    return False
                r += delta[0]
                c += delta[1]
        return True
