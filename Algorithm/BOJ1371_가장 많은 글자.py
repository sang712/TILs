counter = {}
try:
    while True:
        sentence = input().strip()
        for str_ in sentence:
            counter.setdefault(str_, 0)
            counter[str_] += 1
except EOFError:
    if ' ' in counter:
        del counter[' '] 

    ans = []
    alphabet_list = sorted(list(counter.items()), key=lambda x: x[1])
    if alphabet_list:
        max_val = max(counter.values())
        for alphabet, val in alphabet_list:
            if val == max_val:
                ans.append(alphabet)
    print(*sorted(ans), sep='')
