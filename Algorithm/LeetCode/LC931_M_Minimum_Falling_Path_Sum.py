'''
처음에 DFS로 구현하였는데 완전탐색을 했기 때문에 시간초과가 났음
셋 중에서 가장 작은 곳을 선택하는 방법으로 진행했으면 됐는데
다시 짠 코드에서는 BFS, DP(?) 를 혼합한 방식으로
위의 3칸 중 가장 작은 수를 계속해서 더해 가면서 다음 행으로 넘어가는 방식을 사용하였음
150ms 소요, 백분위 87.56%
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for r in range(1, n):
            for c in range(n):
                sc = c - 1 if c > 1 else 0
                ec = c + 1 if c < n - 1 else n - 1
                matrix[r][c] += min(matrix[r-1][sc:ec+1])
        print(matrix)
        return min(matrix[n-1])