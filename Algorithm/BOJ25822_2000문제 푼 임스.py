'''
전혀 풀이방법이 떠오르지않아 검색을 통해 풀이를 확인하고 구현함
누적합일거라 생각은 했지만 스트릭을 기준으로 누적합을 할 것이라는 생각은 꿈에도 못 꿔봤음

검색한 대로 누적합을 구현하고 투포인터를 사용하여 구현했지만 실수를 많이 하여 오답을 3번이나 제출했음
* 첫째로 누적합으로 값을 계산할 때, 포인터에 해당 하는 값을 바로 사용하는 것이 아니라 하나 뒤의 값을 사용해야 하므로
left를 0부터 시작하거나, while문 내에서 left를 -1한 값으로 사용해야 함
* 둘째로 누적합을 만들 때 다음 인덱스의 값은 계속해서 직전 값을 포함하고 있어야 하며, 특정 조건일 때 값을 더해주는 식으로 구현해야함
* 셋째로 지금 사용한 투 포인터는 양 끝에서 시작하는 것이 아니라 둘 다 왼쪽에서 시작하고 있으므로 
while문의 탈출 조건은 right가 리스트의 길이보다 길 경우임
'''
C = int(float(input())//0.99)
if C > 2: C = 2

N = int(input())
problems = list(map(int, input().split()))

max_problems = max(problems)

acc_need_freeze = [0] * (len(problems) + 1)
for i in range(N):
    acc_need_freeze[i + 1] = acc_need_freeze[i]
    if problems[i] == 0:
        acc_need_freeze[i + 1] += 1

max_streaks = 0
left, right = 0, 1
while right <= N:
    if acc_need_freeze[right] - acc_need_freeze[left] <= C:
        max_streaks = max(max_streaks, right - left)
        right += 1
    else:
        left += 1

print(max_streaks, max_problems, sep='\n')