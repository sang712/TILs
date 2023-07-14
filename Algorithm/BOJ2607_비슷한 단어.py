"""
변수명을 비슷한 이름으로 짓지 않도록 해야하겠음

추가로 길이가 같을 때는 문자 하나가 바뀌었을 때 차이가 2개만큼 난다고 카운트 하게 되므로
길이가 같을 때는 2, 길이가 다를 때는 1이하의 차이를 보이는 값을 찾도록 수정하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
the_word = input()
count_the_word = {}
for alpha in the_word:
    count_the_word.setdefault(alpha, 0)
    count_the_word[alpha] += 1
    
cnt = 0
for _ in range(N - 1):
    word = input()
    count_a_word = {}
    for alpha in word:
        count_a_word.setdefault(alpha, 0)
        count_a_word[alpha] += 1
        
    difference = 0
    for ascii in range(26):
        alpha = chr(ascii + 65)
        if alpha in count_the_word:
            if alpha in count_a_word:
                difference += abs(count_a_word[alpha] - count_the_word[alpha])
            else:
                difference += count_the_word[alpha]
        elif alpha in count_a_word:
            difference += count_a_word[alpha]
    
    if len(the_word) == len(word) and difference <= 2 or len(the_word) != len(word) and difference <= 1:
        cnt += 1
print(cnt)
