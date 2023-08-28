"""
맨 뒤 x자리만 잘라서 저장하게 되면 맨뒤 x자리까지만 정확하게 알 수 있음
앞의 유효숫자들은 다 잘려나가기 때문
근데 이 문제는 맨 뒤의 0을 지워야하기 때문에 더 많은 x를 알고 있어야 함
한번에 잘려나가는 0의 개수를 알면 유효숫자를 유지할 수 있음
제한 조건에 따르면 1,000,000(백만)이하의 수를 곱하게 되는데 이 때
최대로 0이 생기는 경우는 390625(5^8)를 곱하는 경우이며 이 때 0이 8개가 생기므로
13자리까지는 알고 있어야 8개를 잘라냈을 때도 5자리의 유효숫자가 유지가 됨

N은 9 이상이므로 5자리 이상이라 슬라이싱을 할 때 따로 조건문을 추가하지 않았음

+) 스트링으로 변환해서 계산하는 것 보다 최대한 int형으로 계산하는 게 더 빠름
"""
N = int(input())

ans = 1
for i in range(2, N + 1):
    ans *= i
    ans = int(str(ans).rstrip('0'))
    ans %= 1_000_00000_00000
print(str(ans)[-5:])