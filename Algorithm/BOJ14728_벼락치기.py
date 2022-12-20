'''
배낭 문제 복습

배낭 문제로 태그되어있는 문제 중 가장 기본적인 배낭문제라고 생각되어 선택하였음

어제 학습한 내용 그대로 코딩하였고 통과하였음
맨 윗 줄에 0이 포함되어있고, 맨 앞 열에도 0이 포함되어있어 
i와 j를 사용할 때 주의해야 한다는 사실을 망각하고 실수를 하여 틀린 답을 제출하였었음
BOJ12865 평범한 배낭 문제보다 주어진 조건이 더 작아서 더 빠르게 통과한 것 같음
556ms 소요되었음
'''
import sys
input = sys.stdin.readline

N, T = map(int, input().split())

total_score_in_time = [[0] * (T+1)]

for i in range(N):
    time, score = map(int, input().split())
    score_in_time = [0]
    for j in range(T):
        if time > j + 1:
            score_in_time.append(total_score_in_time[i][j + 1])
        else:
            score_in_time.append(max(total_score_in_time[i][j + 1], total_score_in_time[i][j + 1 - time] + score))
    total_score_in_time.append(score_in_time)
    
print(total_score_in_time[N][T])