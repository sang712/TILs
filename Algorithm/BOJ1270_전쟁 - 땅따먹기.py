"""
dictionary 자료구조를 Counter 처럼 사용한 뒤에
가장 큰 값을 가지는 키-값 쌍을 하나 가져와서 조건에 맞게 비교한 뒤에 출력하였음
"""
import sys
input = sys.stdin.readline

for n in range(int(input())):
    T, *countries = input().split()
    military_force = {}
    for force in countries:
        military_force.setdefault(force, 0)
        military_force[force] += 1
    max_force = max(military_force.items(), key=lambda x: x[1])
    total_force = sum(military_force.values())
    if max_force[1] > total_force / 2:
        print(max_force[0])
    else:
        print('SYJKGW')
