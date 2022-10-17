'''
굳이 알파벳을 사용하는 딕셔너리를 사용하지 않고 ord()함수를 이용해
숫자로 변환하여 리스트에 넣는 방법으로 체크하였음
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [0] * 26
        for str_ in sentence:
            alphabet[ord(str_) - ord('a')] += 1
        return False if 0 in alphabet else True