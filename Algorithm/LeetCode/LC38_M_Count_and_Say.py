'''
말 그대로 구현하였음
시간복잡도가 커서 고민했는데 n의 범위가 작아서 가능했음
56ms 소요
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        dp= [0, '1']
        for i in range(1, n):
            string = dp[i]
            temp = ""
            cnt = 1
            for j in range(len(string)):
                str_ = string[j]
                if j < len(string)-1:
                    if str_ == string[j+1]:
                        cnt += 1
                    else:
                        temp += str(cnt) + str_
                        cnt = 1
                else:
                    temp += str(cnt) + str_
            dp.append(temp)
        return dp[n]