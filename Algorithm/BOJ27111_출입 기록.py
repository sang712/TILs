"""
a의 최대 개수를 길이로 하는 리스트의 값들을 0으로 초기화하여
0과 1의 스위칭 방식으로 문제에서 요구하는 부분을 카운팅하려고 하다가
20만개의 길이면 메모리 낭비가 있을 수 있겠다 생각하여 딕셔너리 자료 구조를 사용함

입력을 받으면서 출입하는 사람이 처음 등장했을 때 0이면 카운팅
기존에 등장했는데 저장된 값과 같다면 카운팅
마지막으로 1로 저장되어있으면 카운팅 하는 방식으로 요구사항을 만족하였고
마지막 카운팅 방식은 map함수에 lambda함수를 적용하여 간편하게 작성하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
in_out_record = {}

ommition = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a in in_out_record:
        if in_out_record[a] == b:
            ommition += 1
    else:
        if b == 0:
            ommition += 1
    in_out_record[a] = b
ommition += sum(map(lambda x: x == 1, in_out_record.values()))
print(ommition)