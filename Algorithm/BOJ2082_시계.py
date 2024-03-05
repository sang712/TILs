"""
그냥 구현을 하려다보니 for문이 너무 깊게 까지 필요하고 그러다보니 사고에 어려움이 생겨 함수로 한 덩이를 나눴음
그리고 좀 더 구현한 함수를 이해하기 쉽도록 만들기 위해서 입력 정보와 비교할 정보를 zip으로 역행렬을 만들어
한 행에 한 숫자가 되도록 만들었음
눈으로 보기에는 zip을 하지 않은 것이 좋지만 머리로 로직을 구현하거나 따라갈 때는 이 방법이 훨씬 편해 그리하였음
"""
diode = [['###', '..#', '###', '###', '#.#', '###', '###', '###', '###', '###'],
         ['#.#', '..#', '..#', '..#', '#.#', '#..', '#..', '..#', '#.#', '#.#'],
         ['#.#', '..#', '###', '###', '###', '###', '###', '..#', '###', '###'],
         ['#.#', '..#', '#..', '..#', '..#', '..#', '#.#', '..#', '#.#', '..#'],
         ['###', '..#', '###', '###', '..#', '###', '###', '..#', '###', '###']]

diode = list(zip(*diode))
time = [0] * 4
clock = [input().split() for _ in range(5)]
clock = list(zip(*clock))

def check(clock, digit):
    for i in range(len(clock)):
        for j in range(3):
            if clock[i][j] == '#' and diode[digit][i][j] == '.':
                return False
    return True

for clock_digit in range(4):
    for digit in range(9):
        if check(clock[clock_digit], digit):
            time[clock_digit] = digit
            break
print(f'{time[0]}{time[1]}:{time[2]}{time[3]}')