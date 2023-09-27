"""
입력을 받아 enuerate하게 저장하였고(지금 와서 생각난 것이지만 그냥 list(enumerate()) 했어도 됐을 듯)
그 후에 정렬하고 다시 정렬한 순서를 함께 저장한 뒤에
위의 enumerate의 index를 기준으로 다시 정렬하여 이 정렬 직전의 index를 현재 순서대로 출력하였음
"""
N = int(input())
A = list(map(int, input().split()))

temp_squence = []
for idx, a in enumerate(A):
    temp_squence.append([a, idx])
    
temp_squence.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    temp_squence[i].append(i)

temp_squence.sort(key=lambda x: x[1])
_, _, P = zip(*temp_squence)
print(*P)