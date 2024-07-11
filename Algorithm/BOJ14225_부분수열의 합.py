"""
그냥 막연하게 부분수열의 합을 구해서 풀이를 하려고 했는데
예제를 만들다 이진수로 모든 수를 나타낼 수 있다는 것이 떠올라서
이진수와 연관지어 풀이를 하였음
"""
N = int(input())
S = list(map(int, input().split()))

sum_sub_sequence = [0]
for i in range(N):
    for j in range(len(sum_sub_sequence)):
        sum_sub_sequence.append(S[i] + sum_sub_sequence[j])
result = set(sum_sub_sequence)
for i in range(2**20+1):
    if not i in result:
        print(i)
        break