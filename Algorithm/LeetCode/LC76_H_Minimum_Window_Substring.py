'''
투 포인터를 이용하여 sliding window 방식으로 풀었음
먼저 투 포인터로 사용될 인덱스 l과 r을 0에 위치시키고 
r을 먼저 움직여 t에 해당하는 문자들을 모두 포함하도록 만든다
그 후에 l을 움직여 [l:r+1]에 해당하는 문자열을 줄여가는데
이 때 t에 해당하는 문자를 제외시켰으면 다시 r을 움직이도록 하고 그 외에 경우에는 반복한다
그렇게해서 가장 짧은 문자열을 얻었을 때 해당 문자열을 return한다
다른 블로그 글보다 느린 것으로 봐서 조금 더 최적화를 할 수 있을 것으로 생각 됨
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        required = dict()
        for c in t:
            required.setdefault(c, 0)
            required[c] += 1
        l, r = 0, 0
        cnt_required = n
        min_len = 100001
        output = ""
        for r in range(m):
            if s[r] in required:
                required[s[r]] -= 1
                if required[s[r]] >= 0:
                    cnt_required -= 1
            while l <= r and cnt_required == 0:
                if min_len > r-l+1:
                    min_len = r-l+1
                    output = s[l:r+1]
                if s[l] in required:
                    required[s[l]] += 1
                    if required[s[l]] > 0:
                        cnt_required += 1
                l += 1
        return output