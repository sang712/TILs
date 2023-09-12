"""
Collections의 Counter를 이용해 문자의 숫자를 바로 세고
값들만 뽑아서 정렬한 뒤에 겹치는 값이 있으면 1씩 줄이면서 카운팅해 나가고
0이면 무시하는 방법으로 결과를 도출하였음
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        frequency = sorted(counter.values(), reverse=True)
        ans = 0
        appeared = {frequency[0], }
        for value in frequency[1:]:
            while value in appeared:
                value -= 1
                ans += 1
                if value == 0:
                    break
            appeared.add(value)
        return ans