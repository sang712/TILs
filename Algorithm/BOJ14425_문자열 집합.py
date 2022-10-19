'''
입력이 최대 20001줄이라 sys.stdin.realine을 사용하였음
개별로 카운팅하는 것이 아니라 dictionary보단 set이 빠를 거 같아서 set을 사용하였음
존재 하는지 하지 않는지만 확인하여 카운팅하였음
140ms 소요
Trie라는 자료구조를 알게 되어서 해당 방법으로 구현하였는데 생각보다 그리 빠르지는 않았음
dictionary를 이용해서 간략하게 구현하였는데 이 때문에 느린 것일 수도 있음
collections의 얕은 복사 특징을 이용해서 다음 노드 다음 노드로 이동하였고,
input에 \n이 포함되는 것을 확인하고 terminal 원소? 속성? 이 없어도 되어 추가하지 않았음
검색하는 과정도 얕은 복사 특징을 이용하여 검색하였음
122MB/1436MB 의 메모리를 사용하였고 5632ms가 걸렸음
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())
cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1
print(cnt)


'''Trie으로 구현한 답안'''
# S = dict()
# for _ in range(N):
#     temp = S
#     for str_ in input():
#         temp.setdefault(str_, dict())
#         temp = temp[str_]

# def searching(string):
#     try:
#         temp = S
#         for str_ in string:
#             temp = temp[str_]
#         return True
#     except:
#         return False
# cnt = 0
# for _ in range(M):
#     if searching(input()):
#         cnt += 1
# print(cnt)