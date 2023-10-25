N = int(input())

# i의 자리수를 j로 시작했을 때 나올 수 있는 경우의 수, 예외 i=1, j=0은 1로 잡음 (두자리수부터 0도 취급되기 때문)
# 위의 이유로 안 되는 0은 예외처리 하였음
# 1022는 find_the_start 함수에서 <로 처리하는 바람에 검출이 안 돼서 예외처리 하였음
cnt = [[0] * 10, [1] * 10]

for i in range(1, 10):
    temp = [0]
    for j in range(1, 10):
        temp.append(sum(cnt[i][:j]))
    cnt.append(temp)

def calculate(kth_digit, acc, ans):
    if N == 0: return 0
    if N == 1022: return 9876543210
    if acc < 0:
        return -1
    if N <= 9: return sum(cnt[1][1:N + 1])
    if kth_digit <= 1:
        return ans
    for j in range(10):
        if acc + cnt[kth_digit - 1][j] < N:
            acc += cnt[kth_digit - 1][j]
        else:
            return calculate(kth_digit - 1, acc, ans * 10 + j)

def find_the_start():
    acc = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if acc + cnt[i][j] < N:
                acc += cnt[i][j]
            else:
                return i, acc, j
    return -1, -1, -1

print(calculate(*find_the_start()))