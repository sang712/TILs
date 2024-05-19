"""
각 줄의 문자를 탐색하면서 숫자형이면 리스트에 저장하고
문자를 만나거나 문장이 끝났을 때 현재까지 저장한 순자형을 모두 합쳐 int형으로 변환한 뒤 따로 저장함
그 후에 따로 저장한 숫자들을 정렬하여 출력하였음
"""
N = int(input())
ans = []
for _ in range(N):
    row = input()
    num = []
    for str_ in row:
        if '0' <= str_ <= '9':
            num.append(str_)
        elif num:
            ans.append(int(''.join(num)))
            num = []
    if num:
        ans.append(int(''.join(num)))
ans.sort()
print(*ans, sep='\n')