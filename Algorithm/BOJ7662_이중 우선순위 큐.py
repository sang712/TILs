'''
역시 heapify를 사용하면 시간초과가 남 프로그래머스 뭔가 빠진 느낌이다
검색을 통해 대부분이 구현한 방법인 min heap과 max heap을 사용하되
동기화하는 방법을 추가한다
동기화는 pushed 리스트(visited와 유사)를 이용, 
연산의 회수를 idx로 삼아서 push가 된 값은 1로, 한 번 pop된 값은 0으로 두고
pushed에 0으로 들어가 있으면 dump 값이 된다고 생각하기
7900ms 소요

deque와 이분탐색으로 구현한 답안도 있었음
'''
import heapq
import sys
input = sys.stdin.readline

T = int(input())
for testcase in range(T):
    Q = []
    max_Q = []
    k = int(input())
    pushed = [0] * (k+1)
    for idx in range(k):
        command, num = input().split()
        if command == 'I':
            heapq.heappush(Q, (int(num), idx))
            heapq.heappush(max_Q, (-int(num), idx))
            pushed[idx] = 1
        elif command == 'D':
            if num == '1':
                while max_Q and not pushed[max_Q[0][1]]:
                    heapq.heappop(max_Q)
                if max_Q:
                    pushed[max_Q[0][1]] = 0
                    heapq.heappop(max_Q)
            elif num == '-1':
                while Q and not pushed[Q[0][1]]:
                    heapq.heappop(Q)
                if Q:
                    pushed[Q[0][1]] = 0
                    heapq.heappop(Q)
    while max_Q and not pushed[max_Q[0][1]]:
        heapq.heappop(max_Q)
    while Q and not pushed[Q[0][1]]:
        heapq.heappop(Q)
    
    if Q:
        print(-max_Q[0][0], Q[0][0])
    else:
        print('EMPTY')
