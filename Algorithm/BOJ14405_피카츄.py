'''
S의 길이가 0인 경우를 처음에 제외시켰고
피카츄가 할 수 있는 말을 다른 문자열로 대체시킨다음 그 문자를 공백으로 대체해서
결과가 빈 문자열인지 아닌지 판단하여 결과를 print 하였음
'''
S = input()

if S == '':
    print("NO")
else:
    S = S.replace("pi", '1')
    S = S.replace("ka", '1')
    S = S.replace("chu", '1')
    S = S.replace('1', '')

    if S == '':
        print("YES")
    else:
        print("NO")