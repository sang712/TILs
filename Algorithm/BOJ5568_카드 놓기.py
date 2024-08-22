"""
조합을 구해 set 자료구조에 넣은 뒤 개수를 출력하였음
"""
import itertools

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

print(len(set(''.join(selected_card) for selected_card in itertools.permutations(cards, k))))