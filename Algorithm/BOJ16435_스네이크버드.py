'''
정렬해서 순차적으로 크기를 비교하기
'''

N, L = map(int, input().split())
fruits = list(map(int, input().split()))
fruits = sorted(fruits)

for fruit in fruits:
    if fruit <= L:
        L += 1
    else:
        break
print(L)