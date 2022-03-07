'''
1. X의 약수를 모두 구한다
1-2. 이 때 X의 절반에 해당하는값까지 for문으로 확인한다
(2로 나눴을 때가 가장 큰 약수가 나오는 때 이므로)
(내가 짠 것(1732ms)과 에라스토스테네스의 체를 적용한 것(1796ms)과는 별 차이가 없었음
2. 서로소인지 확인한다
------------------------------------------
2번 과정에서 실수가 있어서 엄청나게 틀렸다
모든 약수를 확인하고 서로소인지 판별은 해야 했는데
나는 그냥 ans[0]값인 X값 자체와만 비교하고 ans에 추가한 꼴이 되어 틀렸다
count로 확인하여 해당 값으로 서로소가 맞는지 결정했다
+) 2번 과정에서 파이썬 math 함수인 gcd 함수를 사용해도 된다고 한다
* math.gcd(X, A) == 1이면 서로소
'''

N = int(input())
As = list(map(int, input().split()))
X = int(input())
ans = []

measures = [X]
for i in range(2, X//2 + 1):
    if X % i == 0:
        measures.append(i)

for A in As:
    count = 0
    for measure in measures:
        if A % measure == 0 or measure % A == 0:  # 서로 약수가 있으면
            count += 1
            break  # 중단
    if count == 0:
        ans.append(A)

print(f'{sum(ans)/len(ans):.7}')  # f-string 방식에서 :으로 출력 방식 조건을 걸 수 있다