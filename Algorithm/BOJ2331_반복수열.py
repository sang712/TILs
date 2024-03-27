"""
수열을 리스트로 만들면서 등장을 판단할 수 있도록 set() 자료 구조에도 저장하였음
이미 한 번 나왔던 숫자이면 수열에서 해당 수의 인덱스를 찾아 출력하도록 하였음
"""
A, P = map(int, input().split())

def next_num(num):
    result = 0
    while num:
        num, digit = divmod(num, 10)
        result += digit ** P
    return result

num_to = set()
num_to.add(A)
sequence = [A]
while True:
    A = next_num(A)
    sequence.append(A)
    if not A in num_to:
        num_to.add(A)
    else:
        print(sequence.index(A))
        break