"""
삼각형의 성립 공식에 따라
세 변의 합이 정해져 있을 때 어느 하나가 그 합의 절반이상이면 안 됨
그래서 반복은 25000까지 가능함

가장 긴 변이 정해지면 나머지 두 변의 합이 같기 때문에
나머지 두 변의 합으로 만들 수 있는 조합의 개수를 세면 됨
이 때 나머지 두 변이 될 수 있는 길이는 
(N - 가장 긴 변 * 2) 보다 크거나 같고, 가장 긴 변보다는 작거나 같아야 하니까
될 수 있는 범위의 조합의 개수는 (가장 긴 변 * 3 - N)이고 
가장 긴 변과 길이가 같을 때를 포함해야 해서 1을 더해 준 (가장 긴 변 * 3 - N + 1)임
이 때 나머지 두 변의 순서는 무시하기 때문에 나누기 2를 해줌
이 때 위의 결과가 홀수면 나머지 두 변의 길이가 같을 때를 무시하게 되기 때문에 계산 결과에 1을 더 더해줌
"""
N = int(input())

triangles = set()
cnt = 0
for max_line in range(N // 3, (N + 1) // 2):
    if (N - max_line) % 2:
        cnt += (3*max_line - N + 1) // 2 if 3*max_line - N >= 0 else 0
    else:
        cnt += (3*max_line - N + 1) // 2 + 1 if 3*max_line - N >= 0 else 0
    # cnt += (3*max_line - N + 1) // 2 + (N - max_line + 1) % 2 if 3*max_line - N >= 0 else 0
        
print(cnt)