"""
2중 for문을 이용해 조합을 짜도록 하였고
set 자료구조를 이용해 중복되는 조합은 걸러내었음
"""
paternal_1, paternal_2 = input().split()
maternal_1, maternal_2 = input().split()

colors = [paternal_1, paternal_2, maternal_1, maternal_2]
possibility = set()
for body in colors:
    for tail in colors:
        possibility.add((body, tail))

for body, tail in sorted(list(possibility), key=lambda x: (x[0], x[1])):
    print(body, tail)