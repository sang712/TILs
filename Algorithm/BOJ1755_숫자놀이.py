"""
숫자를 문자로 전환할 수 있도록 딕셔너리 자료 구조를 사용했고
숫자와 문자로 전환된 숫자를 쌍으로 다시 새로운 딕셔너리 자료 구조에 저장하였음
그 후에 items() 함수로 값을 뽑아내 값을 기준으로 정렬을 하고
출력시에는 키값만 나올 수 있도록 zip함수를 사용하였음
"""
M, N = map(int, input().split())

num_to_word = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', 
               '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
numbers = {}
for num in range(M, N+1):
    temp = ''
    for s in str(num):
        temp += num_to_word[s]
    numbers[num] = temp

ans = sorted(list(numbers.items()), key=lambda x: x[1])
for i in range(0, len(ans), 10):
    print(*list(zip(*ans[i:i+10]))[0])