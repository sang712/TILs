'''
처음에는 중복된 문자열은 중앙에 1개만 배치할 수 있다고 생각했는데 짝수개이면 양 옆으로 배치할 수 있어서 
set으로 설정하여서 처음 나오면 넣고 같은 것이 나올 때마다 지워주면서 길이를 4씩 늘였음
그리고 마지막에 1개라도 남으면 길이를 2씩 늘렸음
양 옆에 짝이 맞는지도 set으로 체크를 했었는데 같은 것이 2번 연속 나오는 꼴의 경우 
체크를 제대로 하지 못 한다는 오류가 있어서 다시 dict로 바꿔준 뒤에 나올 때마다 카운트를 해주고
반대편 것이 나왔다면 체크를 해서 없애는 방식으로 진행하였음
'''
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        double = set()
        checkingPelindrome = dict()
        length = 0
        for word in words:
            if word[0] == word[1]:
                if word in double:
                    double.remove(word)
                    length += 4
                else:
                    double.add(word)
            else:
                drow = word[1] + word[0]
                if drow in checkingPelindrome:
                    if checkingPelindrome[drow] > 0:
                        checkingPelindrome[drow] -= 1
                        length += 4
                    else:
                        checkingPelindrome.setdefault(word, 0)
                        checkingPelindrome[word] += 1
                else:
                    checkingPelindrome.setdefault(word, 0)
                    checkingPelindrome[word] += 1
        if double:
            length += 2
        return length
