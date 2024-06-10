"""
우선 딱 붙어 있는 소들을 제거하고
맨 앞에서 탐색했을 때 중간에 1번씩만 나오는 소들의 마릿수를 세서 답에 포함시켰음
무턱대고 등장하기만 하면 세는 방식으로 했더니 틀린 답이었음
"""
cattles = input()

checking = []
for cattle in cattles:
    if checking and checking[-1] == cattle:
        checking.pop()
    else:
        checking.append(cattle)

ans = 0
while checking:
    cattle = checking.pop(0)
    second_spot = checking.index(cattle)
    counter = set()
    for i in range(second_spot):
        cattle = checking[i]
        if cattle in counter:
            counter.discard(cattle)
        else:
            counter.add(cattle)
    ans += len(counter)
    checking.pop(second_spot)
print(ans)