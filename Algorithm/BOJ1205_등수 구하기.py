"""
생각해야할 조건이 많은 문제였음
첫째로 0 <= N <= P 이어서 N이 0일 경우 두번째 줄 입력이 없기 때문에
해당 부분을 걸러내야 하고
둘째로 N과 P가 같을 때 새로 낸 점수가 마지막 랭킹 리스트의 점수와 같다면
이 부분에서도 -1을 출력해야한다는 점을 고려해서 조건문을 짜야했음

그리고 조건문 중 다음과 같은 부분은
(N == P and new_score > ranking_list[P - 1]) or N < P
or 이후의 문이 만족하지 않으면 초기 조건에 따라 N == P도 만족한다는 것으로
다음 문제 풀이와 같이 or의 순서를 바꾸고 더 짧게 작성하였음
"""
N, new_score, P = map(int, input().split())

rank = 1
if N > 0:
    ranking_list = sorted(list(map(int, input().split())), reverse=True)
    if N < P or new_score > ranking_list[P - 1]:
        for score in ranking_list:
            if score <= new_score:
                break
            rank += 1
    else:
        rank = -1
print(rank)
        