import sys
input = sys.stdin.readline

password = input().rstrip()
while not password == 'END':
    pass_list = list(password)
    pass_list = reversed(pass_list)
    print(''.join(pass_list))
    password = input().rstrip()