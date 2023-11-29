"""
부동소수점을 처리하여 오차가 없도록 계산하는 문제

여러번 제출해도 틀려서 무엇이 문제인지 확인하느라 오래 걸렸음

일단 문제에서 입력으로 주어진 평균 값은 소수점 4째자리부터 버림된 것임
그래서 사람의 수 * 평균 값을 했을 때 
온전한 그 값이 나올 수도
온전한 그 값의 소숫점 자릿수를 올림한 수일 수도 있음

처음 문제를 풀 때, 온전한 그 값 중 딱 떨어지는 경우만 확인했기 때문에 틀린 답을 냈는데
온전한 그 값이 딱 안 떨어지고 버림 해야 하는 값이 있을 때를 확인하는 경우를 추가하니 맞았음

그리고 브루트포스로 풀이 했는데도 시간이 오래 걸리진 않았음
"""
import sys
input = sys.stdin.readline

N = int(input())
averages = []
for _ in range(N):
    _, decimal = input().strip().split('.')
    averages.append(decimal)

for people in range(1, 1001):
    for average in averages:
        average = int(average)
        sumation = average * people
        if sumation % 1000 == 0:
            pass
        elif (sumation // 1000) * 1000 // people == average:
            pass
        elif (sumation // 1000 + 1) * 1000 // people == average:
            pass
        else:
            break
    else:
        print(people)
        break
