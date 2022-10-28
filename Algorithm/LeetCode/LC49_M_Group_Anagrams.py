'''
set을 사용할까 했는데 같은 알파벳을 여러번 사용할 경우 사라지는 경우가 생겨서 다른 방식을 생각함
단어를 sort해서 key로 사용하는 것
단어를 sort하고(list로 변환됨) 다시 join으로 합친 뒤에 key로 사용함
setdefault를 사용하여 4줄짜리 if-else구문을 2줄로 만들었는데 204ms이고
4줄짜리를 사용할 때 202ms로 2ms가 더 빨라서 이 방식을 최종 답안으로 선택하였음
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word = dict()
        for word in strs:
            key = ''.join(sorted(word))
            if not key in sorted_word:
                sorted_word[key] = [word]
            else:
                sorted_word[key].append(word)
        return sorted_word.values()