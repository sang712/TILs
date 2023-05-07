"""
수열의 규칙을 찾아 해당 수가 입력으로 주어진 수만큼 등장했을 때의 자리를 구하는 문제
규칙을 찾아 주어진 수와 구하려는 수와의 차이가 큰 경우는 단순 계산으로 생략하도록 하였고
차이가 좁아진 경우에 값을 하나하나 늘려가며 구하려는 수와 비교하여 반복문을 탈출하도록 하였고
마지막에 인원으로 나누어 떨어진 나머지를 출력하였음

중간에 생각하지 못했던 부분이 중간에 break문을 탈출하지 못했을 때
변수가 어떻게 바뀌어나 하나인데 for문 들어가기 전의 덧셈을 누락하여 문제를 틀렸었음
반례는
3
3
0
출력되는 답은 0이 나와야 함
"""
A = int(input())
T = int(input())
phrase = int(input())

n = 0
num_passed_people = 0
cnt_phrase = 0
while True:
    n += 1
    if T > cnt_phrase + 2 + (n + 1):
        cnt_phrase += 3 + n
        num_passed_people += 2 * (3 + n)
        continue
    
    cnt_phrase += 1
    num_passed_people += 1
    if cnt_phrase == T:
        if phrase:
            num_passed_people += 1
        break
    cnt_phrase += 1
    num_passed_people += 2
    if cnt_phrase == T:
        if phrase:
            num_passed_people += 1
        break
    num_passed_people += 1
    for i in range(1, n + 2):
        if cnt_phrase + i == T:
            num_passed_people += i
            if phrase:
                num_passed_people += n + 1
            break
    break
print((num_passed_people - 1) % A)