"""
나선형으로 돌아가면서 숫자를 뱉어내는 방식으로 구현을 했다가
요구사항이 0부터라는 것을 알게 되어 쓸데 없는 짓이라는 것을 알게 되었고
최대값인 백만 백만을 입력으로 넣어서 시간이 오래걸리는 것을 확인 하였음
그래서 좌표간 규칙을 찾아 새롭게 구현하였고
기존에 구현한 내용은 검산용으로 놔 둠
"""
puppy_x, puppy_y = map(int, input().split())
# monkey = 1
# guess_x, guess_y = 0, 0

# delta = [(-1, 1), (-1, 0), (0, -1), (1, -1), (1, 0), (0, 1)]
# def is_same_pos(x1, y1, x2, y2):
#     if x1 == x2 and y1 == y2:
#         return True
#     return False

# round = 1
# while True:
#     if is_same_pos(puppy_x, puppy_y, guess_x, guess_y):
#         break
    
#     monkey += 1
#     guess_y += 1
#     if is_same_pos(puppy_x, puppy_y, guess_x, guess_y):
#         break
    
#     for i in range(len(delta)):
#         if is_same_pos(puppy_x, puppy_y, guess_x, guess_y):
#             break
        
#         dx, dy = delta[i][0], delta[i][1]
#         if i:
#             for _ in range(round):
#                 monkey += 1
#                 guess_x += dx
#                 guess_y += dy
#                 if is_same_pos(puppy_x, puppy_y, guess_x, guess_y):
#                     break
#         else:
#             for i in range(round - 1):
#                 monkey += 1
#                 guess_x += dx
#                 guess_y += dy
#                 if is_same_pos(puppy_x, puppy_y, guess_x, guess_y):
#                     break
#     round += 1
# print(monkey)

ans = 1
y_coeff = 0
for j in range(puppy_y):
    y_coeff += j + 1

const = max(puppy_y - 1, 0)
x_coeff = 0
for i in range(puppy_x):
    x_coeff += (i + 1 + const)

ans += 6 * (x_coeff)
print(ans)