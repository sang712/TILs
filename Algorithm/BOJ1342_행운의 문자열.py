"""
답을 공식으로 쉽게 구할 수 있는 경우 해당 답을 계산하여 출력하였고
그렇지 않을 때만 골라 직접 경우의 수를 찾아 출력하도록 하였음
"""
S = input()

counter = {}
for s in S:
    counter.setdefault(s, 0)
    counter[s] += 1

if max(counter.values()) > (len(S) + 1) // 2:
    print(0)
elif max(counter.values()) == 1:
    ans = 1
    for i in range(2, len(S) + 1):
        ans *= i
    print(ans)
else:
    string_list = list(counter.keys())
    ans = 0
    def align():
        global ans
        if len(result) == len(S):
            ans += 1
            return
        for s in string_list:
            if result and result[-1] == s:
                continue
            if counter[s]:
                result.append(s)
                counter[s] -= 1
                align()
                result.pop()
                counter[s] += 1
    result = []
    align()
            
    print(ans)