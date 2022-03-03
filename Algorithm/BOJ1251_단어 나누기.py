'''
1. 단어를 3개로 나눈다.
1-2. 단어를 3개로 나누는 방식은 for문 2개로 이동식 인덱스로 구현
2. 나눈 단어를 각각 reversed 내장함수로 변환 시킴
2-2. reversed 내장함수를 사용하게 되면 reversed 형으로 반환되기 때문에 후처리가 필요함
2-3. list나 tuple의 경우는 명시적 형변환을 통해 후처리를 하면 되고 스트링의 경우는 ''.join() 함수로 묶어주면 됨
3. 스트링의 비교를 하면 알아서 사전순으로 비교를 해주기 때문에 바로 비교를 하여 갱신하는 형식으로 하였음
'''

word = input()

preceding = ''
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first = ''.join(reversed(word[0:i]))
        middle = ''.join(reversed(word[i:j]))
        last = ''.join(reversed(word[j:len(word)]))

        recombination = first + middle + last

        if i == 1 and j == 2:
            preceding = recombination
        elif preceding > recombination:
            preceding = recombination

print(preceding)

