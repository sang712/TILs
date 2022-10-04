'''
람다를 이용해 소트를 하는 방법을 다시 익힘
4자리 번호가 주어진 문제는 입력에 \n이 포함되어 있어서 이부분 주의하기
'''
import sys
input = sys.stdin.readline

N = int(input())
words = set()

for _ in range(N):
  str_ = input().strip()
  words.add(str_)

words = list(words)
words.sort(key = lambda x: (len(x), x))
for word in words:
  print(word)