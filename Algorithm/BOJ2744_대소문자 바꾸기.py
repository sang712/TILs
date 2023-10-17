sentence = input()
ans = []
for s in sentence:
    if s.islower():
        ans.append(s.capitalize())
    else:
        ans.append(s.lower())
print(''.join(ans))