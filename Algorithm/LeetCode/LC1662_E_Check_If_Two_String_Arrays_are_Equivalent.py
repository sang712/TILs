'''
주어진 각 list들을 순회하면서 새 string 변수에 더해주었는데
이보다 더 효율적인 방법으로 파이썬의 함수인 join()함수를 쓰는 방법이 있었음
75ms 에서 61ms로 개선됨
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # word_1, word_2 = '', ''
        # for str_ in word1:
        #     word_1 += str_
        # for str_ in word2:
        #     word_2 += str_
        # return word_1 == word_2
        word1 = "".join(word1)
        word2 = "".join(word2)
        return word1 == word2
