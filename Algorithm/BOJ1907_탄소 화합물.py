"""
입력을 잘 파싱해서 그냥 3중 for 문으로 확인하고 답을 출력하였음
답의 크기가 10 * 10 * 10 이라 그냥 브루트포스로 모든 답을 확인하였음
"""
formula = list(input())

molecule = [None] + [{'C': 0, 'H': 0, 'O': 0} for _ in range(3)]

char = formula.pop()
while char != '=':
    if char.isdigit():
        alpha = formula.pop()
        molecule[3][alpha] += int(char)
    else:
        molecule[3][char] += 1
    char = formula.pop()
char = formula.pop()
while char != '+':
    if char.isdigit():
        alpha = formula.pop()
        molecule[2][alpha] += int(char)
    else:
        molecule[2][char] += 1
    char = formula.pop()
while formula:
    char = formula.pop()
    if char.isdigit():
        alpha = formula.pop()
        molecule[1][alpha] += int(char)
    else:
        molecule[1][char] += 1
c1, h1, o1, = molecule[1]['C'], molecule[1]['H'], molecule[1]['O']
c2, h2, o2, = molecule[2]['C'], molecule[2]['H'], molecule[2]['O']
c3, h3, o3, = molecule[3]['C'], molecule[3]['H'], molecule[3]['O']
ans = None
for x1 in range(1, 11):
    for x2 in range(1, 11):
        for x3 in range(1, 11):
            if c1*x1 + c2*x2 == c3*x3 and h1*x1 + h2*x2 == h3*x3 and o1*x1 + o2*x2 == o3*x3:
                ans = (x1, x2, x3)
            if ans:
                break
        if ans:
            break
    if ans:
        break
print(*ans) 