'''
알파벳의 아스키 코드값을 활용해 리스트의 인덱스로 사용하였고
값을 저장하는 위치에따라 달라지는 전위, 중위, 후위 순회를 하나의 함수로 구현하였음
'''
import sys
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(26)]
for _ in range(N):
    parent, left_child, right_child = input().split()
    tree[ord(parent) - ord('A')].append(left_child)
    tree[ord(parent) - ord('A')].append(right_child)
    
anterior, medial, posterior = [], [], []

def tour_tree(idx: int) -> None:
    anterior.append(chr(idx+65))
    
    left_child, right_child = tree[idx]
    
    if not left_child == '.':
        tour_tree(ord(left_child)-ord('A'))
    medial.append(chr(idx+65))
    
    if not right_child == '.':
        tour_tree(ord(right_child)-ord('A'))
    posterior.append(chr(idx+65))

tour_tree(0)
print(''.join(anterior))
print(''.join(medial))
print(''.join(posterior))