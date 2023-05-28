"""
처음에 map과 sum을 이용해서 X를 문자열으로 변환하고 다시 정수형으로 변환하는 과정에서
str(X) 에서 시간 소요가 많이 되었을 것이라고 생각함 문자열이 길 수록 드는 시간이 많이 들기 때문에

그래서 다른 사람의 답을 찾아보았더니 X를 str자체로 사용하면서 for문으로 접근하는 방식이라
한 문자씩만을 str로 변환하다보니 시간초과가 나지 않음

+) 추가로 X = str(num) 부분을 X = int(num)으로 하고 vscode로 동작시켰을 때는 문제가 없었는데
백준에서 돌리니 typeError가 났음
이런 이슈들은 vscode 상에서 처리를 하는 것 같음
"""
# pypy3 통과 코드
"""
X = input()

cnt = 0
X = int(input())

cnt = 0
while X > 9:
    cnt += 1
    X = sum(map(int, str(X)))
print(cnt)
print('YES' if X % 3 == 0 else 'NO')
"""
X = input()

cnt = 0
while len(X) > 1:
    cnt += 1
    num = 0
    for x in X:
        num += int(x)
    X = str(num)
print(cnt)
print('YES' if int(X) % 3 == 0 else 'NO')