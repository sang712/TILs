"""
괄호가 등장하면 괄호에 따라 점수를 누적하다가
숫자가 나오면 그 때 최대 점수를 갱신하는 방법으로 풀이하였음
"""
S = input()

cur_score = 0
max_score = 0
for s in S:
    if s == '(': cur_score += 1
    elif s == ')': cur_score -= 1
    elif s == '{': cur_score += 2
    elif s == '}': cur_score -= 2
    elif s == '[': cur_score += 3
    elif s == ']': cur_score -= 3
    elif '0' <= s <= '9':
        max_score = max(cur_score, max_score)
print(max_score)