"""
문자열을 합쳐서 새로운 문자열을 만들면 시간이 오래 걸리므로 해당 방법은 최대한 지양하였음
그래서 두 문자열로 무한 문자열을 만들었다고 가정하고
길이의 최소공배수만큼 반복하면서 해당 인덱스가 대표하는 문자를 비교하였음
한 번이라도 어긋났다면 0을 출력하도록 했고
while문 탈출 조건때문에 0번 인덱스는 비교를 못 했는데
while-else문의 else문에서 해당 부분을 마지막으로 체크하도록 하였음
"""
s = input()
t = input()
len_s = len(s)
len_t = len(t)

i = 1
while i%len_s != i%len_t or i%len_t != 0:
    if s[i%len_s] == t[i%len_t]:
        i += 1
        continue
    print(0)
    break
else:
    if s[0] == t[0]:
        print(1)
    else:
        print(0)
     