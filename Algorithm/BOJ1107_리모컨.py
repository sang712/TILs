"""
완전 탐색을 하여도 시간내에 해결 가능한 문제여서 완전 탐색을 하도록하였고
각 숫자들의 자릿수가 고장나지 않은 버튼인지 확인하였고
고장나지 않은 버튼으로만 이루어져있다면 버튼 누른 횟수를 비교하여 더 작은 수를 저장하도록 하였음

이 방법도 가능한데 시간이 너무 오래걸릴 것 같아서 중간에 건너뛰는 방법을 생각하였고
그 방법으로 만약 자릿수가 고장난 버튼이라면 해당 자릿수에서 1을 올리는 방법을 적용하였음
"""
N = int(input())
M = int(input())

broken_buttons = set(input().split()) if M else set()

ans = abs(N - 100)
num = 0
num_loop = 0
while num < 1_000_001:
    num_loop += 1
    str_num = str(num)
    length = len(str_num)
    for idx, digit in enumerate(str_num):
        if digit in broken_buttons:
            num += 10 ** (length - idx - 1)
            break
    else:
        num_key_pushed = length + abs(num - N)
        if ans > length + abs(num - N):
            ans = num_key_pushed
        elif num > N:
            break
        num += 1
print(ans)