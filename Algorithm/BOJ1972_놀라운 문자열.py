def amazing_string(istr):
    N = len(istr)
    D = 0
    if N == 1 or N == 2:
        return True
    while D < N - 1:
        pairs = set()
        for i in range(N-D-1):
            pair = istr[i] + istr[i+D+1]
            pairs.add(pair)
        if len(pairs) < N - D - 1:
            return False
        D += 1
    return True


string = ''
strings = []
while not(string == '*'):
    if string: strings.append(string)
    string = input()
for string in strings:
    is_amazing = amazing_string(string)
    surprising = 'surprising.' if is_amazing else 'NOT surprising.'
    print(f'{string} is {surprising}')
    