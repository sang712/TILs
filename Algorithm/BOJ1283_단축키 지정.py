"""
스트링 ' '은 true 임을 망각하여 틀렸음

공백을 기준으로 나눠서
각 단어의 첫글자를 확인하여 대괄호를 포함하여 답으로 저장하였고

나눠진 단어들을 다시 하나의 스트링으로 만들어
각 문자를 확인하면서 대괄호를 포함하도록 하였고 ' '인 경우에는 생략하였음

마지막으로 아무런 조건에 해당하지 않아도 답에 포함하도록 하여 모든 결과를 출력할 수 있도록 하였음
"""
N = int(input())

commands = set()
ans = []
for _ in range(N):
    option = input().split()
    for i in range(len(option)):
        word = option[i]
        target = word[0].upper()
        if not target in commands:
            commands.add(target)
            option[i] = f'[{option[i][0]}]' + option[i][1:]
            ans.append(' '.join(option))
            break
    else:
        option = ' '.join(option)
        for i in range(len(option)):
            s = option[i]
            target = s.upper()
            if target != ' ' and not target in commands:
                commands.add(target)
                option = option[:i] + f'[{option[i]}]' + option[i + 1:]
                ans.append(option)
                break
        else:
            ans.append(option)
print(*ans, sep='\n')