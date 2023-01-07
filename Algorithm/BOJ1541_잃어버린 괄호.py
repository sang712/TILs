'''
처음엔 덧셈 뺄셈에 괄호를 빼봤자 똑같지 라고 생각했는데
마이너스 뒤의 수들을 다 묶어서 더한 뒤에 마이너스하면 최솟값을 만들 수 있다는 것을 깨달았음

우선 split으로 쪼개서 int형으로 변환을 해주어야 하는데 
동시에 '+'와 '-'를 기준으로 split을 할 수는 없기 때문에 
순서를 정해야했음
고민한 결과 우선 '-'를 기준으로 나누기로 하였는데, 
이는 '+'로 엮인 숫자들을 모두 더한 뒤에 앞의 '-'가 있을 때 음수로 만들어서 빼면 최소가 되기 때문임
그래서 '-'로 split한 결과의 첫번째 수만 따로 더해놓고 나머지 수들은 for문을 돌면서 빼는 방식으로 구현하였음
'''
expressions = list(input().split('-'))

result = sum(map(int, expressions.pop(0).split('+')))
for expression in expressions:
    sumation = sum(map(int, expression.split('+')))
    result -= sumation
print(result)