"""
문자열로 받아서 dictionary 자료 구조에 카운트 하는데
6과 9는 같은 키에 카운트해서
마지막에 1을 더한뒤 2로 나누는 연산으로 처리하였음
"""
N = input()
numbers = {}
for char in N:
    if char == '9':
        numbers.setdefault('6', 0)
        numbers['6'] += 1
    else:
        numbers.setdefault(char, 0)
        numbers[char] += 1

if '6' in numbers:
    numbers['6'] = (numbers['6'] + 1) // 2
print(max(numbers.values()))