"""
1:1 매칭이 되는 숫자와 문자를 미리 리스트 자료 구조를 이용해 만들고
코드와 평문의 길이가 같다는 점을 이용해
어느 하나의 각각의 문자의 개수를 세어 딕셔너리 자료 구조에 저장하고
다른 하나를 세면서 저장했던 딕셔너리 자료 구조와 비교하여
다른 점이 있다면 n 같다면 y를 출력하도록 하였음
"""
decoder = [' ', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

N = int(input())
code = list(map(int, input().split()))
decoded_code = {}
for c in code:
    decoded_code.setdefault(decoder[c], 0)
    decoded_code[decoder[c]] += 1
    
for char in input():
    if char in decoded_code and decoded_code[char] > 0:
        decoded_code[char] -= 1
    else:
        print('n')
        break
else:
    print('y')