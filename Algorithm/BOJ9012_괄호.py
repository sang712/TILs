N = int(input())

def checkingVPS(ps):
    pairs = []
    for p in ps:
        if p == '(':
            pairs.append(p)
        elif p == ')':
            if len(pairs) >= 1:
                parenthesis = pairs.pop(-1)
                if parenthesis == '(':
                    continue
                else:
                    return "NO"
            else:
                return "NO"
    return "YES" if pairs == [] else "NO"

            
for testcase in range(N):
    PS = input()
    print(checkingVPS(PS))