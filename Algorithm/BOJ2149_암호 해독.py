"""
문제에서 설명한 내용을 거꾸로 따라가면서 구현하였음
우선 입력을 받아서 키값을 인덱스값과 함께 정렬을 하였고
암호화 된 값을 받아서 반복문을 이용해 열의 길이 만큼씩 잘라 행의 형태로 리스트에 저장했음
그 후에 zip함수로 열의 형태로 바꿔주면서 동시에 join함수로 각 행이 하나의 단어가 되게 하였고
그 다음에 한 번 더 join 함수를 사용해 모든 행이 하나의 문장이 되도록 하였음
"""
_key = input()
encripted = input()

sorted_key = sorted(enumerate(_key), key=lambda pair: pair[1])

n_col = len(_key)
n_row = len(encripted)//n_col

code = [''] * n_col
for i in range(n_col):
    code[sorted_key[i][0]] = encripted[i*n_row:(i+1)*n_row]
print(''.join(map(''.join, zip(*code))))