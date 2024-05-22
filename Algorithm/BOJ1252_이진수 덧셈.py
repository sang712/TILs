"""
주어지는 두 개의 이진수를 리스트 자료 구조에 각각 담은 뒤 
리스트의 길이를 두 수의 최대길이보다 1길도록 만들어 준 뒤
뒤에서부터 더해서 앞으로 가산하는 방식으로 구현하였음
"""
a, b = input().split()
len_a, len_b = len(a), len(b)
max_len = max(len_a, len_b)

a = ['0'] * (max_len - len(a) + 1) + list(a)
b = ['0'] * (max_len - len(b) + 1) + list(b)
result = ['0'] * (max_len + 1)
add = '0'
for i in range(max_len, -1, -1):
    if a[i] == b[i]:
        result[i] = '1' if add == '1' else '0'
        add = '1' if a[i] == '1' else '0'
    else:
        result[i] = '0' if add == '1' else '1'
print(int(''.join(result)))
