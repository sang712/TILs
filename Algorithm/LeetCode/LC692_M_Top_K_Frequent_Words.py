'''
dictionary를 이용하여 같은 문자열끼리 카운팅을 하고
items()함수를 이용해 key, value값의 튜플쌍을 원소로하는 list를 만들고
해당 list를 정렬한 뒤 zip으로 key값들로만 list로 만들고
k개수만큼 잘라서 return하였음
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = dict()
        for word in words:
            cnt.setdefault(word, 0)
            cnt[word] += 1
        out = list(cnt.items())
        out.sort(key=lambda x: (-x[1], x[0]))
        out = list(zip(*out))
        return out[0][:k]