"""
접미사 배열과는 다르게 접두사 배열은 시작하는 문자가 같기때문에
정렬을 해도 무조건 순서대로 나옴
따라서 s의 길이만큼 그냥 숫자를 출력하였음
"""
s = input()
print(*range(len(s)), sep='\n')