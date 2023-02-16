"""
최초로 같게 등장하는 부분만 체크하면 되므로
해당 부분을 슬라이싱하여 비교하고
같다면 타겟 단어의 길이 만큼 건너뛰도록 구현하였음
"""
document = input()
target_word = input()

d_len = len(document)
t_len = len(target_word)
i = 0
count = 0
while i < d_len:
    if document[i:i+t_len] == target_word:
        i += t_len
        count += 1
        continue
    i += 1
print(count)