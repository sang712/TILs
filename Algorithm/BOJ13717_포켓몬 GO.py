"""
딕셔너리 자료구조로 정보를 저장한 뒤에 정렬하여 원하는 내용만 사용하도록 하였음
특히 도감 순서대로 정렬하는 것은 따로 입력이 주어지지 않았기 때문에
임의로 등장 순서에 번호를 부여하여 정렬에 사용하도록 하였음
"""
import sys
input = sys.stdin.readline

dict_pokemon = {}
total_evolution = 0
for n in range(int(input())):
    pokemon = input().strip()
    acquired, possessed = map(int, input().split())
    unit_total_evolution = 0
    while acquired <= possessed:
        num_evolution = possessed // acquired
        possessed = possessed % acquired + num_evolution * 2
        unit_total_evolution += num_evolution
    total_evolution += unit_total_evolution
    dict_pokemon[pokemon] = (n, unit_total_evolution)
    
pokemon_encyclopedia = sorted(list(dict_pokemon.items()), key=lambda x: (-x[1][1], x[1][0]))

print(total_evolution)
print(pokemon_encyclopedia[0][0])
