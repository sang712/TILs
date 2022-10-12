'''
각 행의 군인 수를 계산하여 군인의 수와 행의 idx를 튜플로 묶어 리스트로 정리하였음
해당 리스트를 군인의 수를 우선으로 하는 오름차순으로 정렬하였고
zip(*list)를 이용해 idx만 뽑아 앞에서 k개의 idx를 반환하였음

key=lambda를 썼을 때(107ms)와 쓰지 않았을 때(254ms)
우선하는 인자만(x[0]) 넣었을 때(256ms) 시간차이가 유의미하게 났음
정렬을 하고자 하는 리스트의 인자가 iterable한 객체면 key=lambda를 쓰고
인자들의 우선순위를 전부 명시하는 것으로
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soliders_row = []
        for i in range(len(mat)):
            cnt = 0
            for p in mat[i]:
                if p: cnt += 1
                else: break
            soliders_row.append((cnt, i))
            
        soliders_row.sort(key = lambda x: (x[0],x[1]))
        soldiers, indices_rows = zip(*soliders_row)
        return indices_rows[:k]