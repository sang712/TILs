# 알아야 할 내용
# dict는 넣은 순서대로 저장이 되어 따로 정렬을 해야한다
# dict는 value를 유지하면서 sort하려면 items를 적용해야 한다
# 이 때 결과물은 튜플 리스트로 반환된다
# f 프린트 사용법을 숙지하자
# print 함수에 f로 시작하는 문자열 f''을 사용하고 내부에 파이썬 표현식을 중괄호로 묶어
# 사용하면 된다. 특정한 형식을 적용하고 싶을 경우 :을 사용하면 된다
# 정수를 : 뒤에 작성하면 최소 문자 폭이 된다
import sys

species_dict = {}
count = 0
while True:
    species = sys.stdin.readline().strip()
    if species == '':
        break
    count += 1
    if species in species_dict:
        species_dict[species] += 1
    else:
        species_dict[species] = 1

sorted_species = sorted(species_dict.items())
for species, value in sorted_species:
    print(f'{species} {value / count * 100:.4f}')
