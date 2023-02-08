"""
스택 문제임을 직감하고 넣은 일련의 문자가 폭발 문자열과 같다면
해당 부분을 pop하는 방식으로 구현하였음

3배 빠른 200ms 대의 코드도 있어서
확인해봤더니 폭탄 문자열의 길이만큼 반복해서 팝하는 게 아니라
del 명령어를 이용해 해당 부분을 한번에 지워버리는 방법으로 구현되어 있었음
그래서 같은 방법을 적용했더니
660ms에서 272ms 까지 시간을 줄일 수 있었음
"""
my_string = input()
bomb = input()

detonator = bomb[-1]
bomb_length = len(bomb)

stack = []
for char in my_string:
    stack.append(char)
    if char == detonator and ''.join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]
            
print(''.join(stack) if stack else 'FRULA')