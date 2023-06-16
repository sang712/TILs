"""
dictionary 자료 구조의 setdefault 함수를 이용해서 
Error 없이 입력을 카운팅 하였고

저장한 내용을 items를 이용해 빼내 정렬한 뒤에 
가장 수가 크고 이름이 앞 순서인 책을 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

books = {}
for _ in range(N):
    book = input().strip()
    books.setdefault(book, 0)
    books[book] += 1
    
book_rank = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(book_rank[0][0])