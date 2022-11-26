'''
포켓몬 번호로 포켓몬을 출력하는 것은 리스트에 저장하여 호출할 수 있도록 하였고
포켓몬 이름으로 출력하는 것은 딕셔너리에 저장하여 호출할 수 있도록 하였음
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_by_num = ['none']
pokemon_by_name = {}

for num in range(N):
  pokemon = input().strip()
  pokemon_by_num.append(pokemon)
  pokemon_by_name[pokemon] = num + 1

for _ in range(M):
  question = input().strip()
  if 65 <= ord(question[0]) <= 90:
    print(pokemon_by_name[question])
  elif 48 <= ord(question[0]) <= 57:
    print(pokemon_by_num[int(question)])
