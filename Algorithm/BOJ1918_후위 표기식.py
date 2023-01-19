"""
괄호 안에 들어있는 식의 계산이 우선시 되기 때문에 괄호를 먼저 없애도록 하였고
괄호를 없앤 뒤에는 연산을 처리하도록 구현하였음
괄호를 없애는 함수와 연산을 처리하는 함수를 각각 구현하여 사용하였음
연산을 처리하는 함수는 우선 곱하기와 나누기를 우선 처리하고 그 뒤에 더하기와 빼기를 처리하였음
두 함수 모두 list와 str을 모두 받을 수 있도록 하였고 대신 문자열을 다루는 과정에서는 list로 변환하여 사용하였음
list로 변환하지 않으면 이미 후위 연산으로 바뀐 식을 하나의 항으로 묶기 어렵기 때문에 이 같은 방법을 사용하였음

답을 좀 더 살펴보니 방식을 일반화하여 깔끔하게 작성된 코드가 있었는데
이해하기 어렵고 시간도 전혀 차이가 나지 않아서 여기에서 마무리 짓도록 함
40ms 소요됨
"""
def med_to_post(exp: list or str) -> str:
    prior = []
    temp = ''
    for i in range(len(exp)):
        if temp:
            prior.append(prior.pop() + exp[i] + temp)
            temp = ''
            continue
        if exp[i] == '*' or exp[i] == '/':
            temp = exp[i]
        else:
            prior.append(exp[i])
    later = []
    for i in range(len(prior)):
        if temp:
            later.append(later.pop() + prior[i] + temp)
            temp = ''
            continue
        if prior[i] == '+' or prior[i] == '-':
            temp = prior[i]
        else:
            later.append(prior[i])
    # print(exp, prior, later)
    return ''.join(later)

def removing_parenteses(expression: str) -> list[str]:
    elements = []
    parenthes = []
    i = 0
    while i < len(expression):
        temp = expression[i]
        if temp == '(':
            parenthes.append(len(elements))
        elif temp == ')':
            j = parenthes.pop()
            temp = [temp]
            while len(elements) > j:
                temp = [elements.pop()] + temp
            temp = med_to_post(temp[1:-1])
            # print(temp, elements)
        elements.append(temp)
        i += 1
    return elements

expression = input()
parentheses = expression.count('(')
if parentheses:
    exp_without_par = removing_parenteses(expression)
else:
    exp_without_par = expression

print(med_to_post(exp_without_par))

"""
첫 반례
입력
A+(C-N*(U-O)+Q)
출력
ACNUO-*-Q++

두번째 반례
입력
(A+B)*C+(D/E)
오답
AB+C*(+DE/
정답
AB+C*DE/+
"""