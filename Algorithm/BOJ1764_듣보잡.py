'''
딕셔너리를 이용해서 카운트 한 뒤에 2번이 카운트 된 것들만 추려서 정렬한 뒤에 출력하였음
입력에 \n이 포함되어 있어 해당 부분을 strip하고 사용하였음 (그렇지 않으면 맨 마지막 것은 따로 카운팅 되므로)
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

people = {}
unknown_people = []

for _ in range(N+M):
  person = input().strip()
  people.setdefault(person, 0)
  if people[person]:
    unknown_people.append(person)
  people[person] += 1

unknown_people.sort()
print(len(unknown_people))
print('\n'.join(unknown_people))
