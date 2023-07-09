"""
파이썬에는 훌륭한 내장함수들이 있어서 split함수로 파싱을 대신하였고
대신 한 자리 수만 들어올 경우 *를 이용해서 받든 안 받든 하는 방식으로 하였고
나머지는 조건에 맞게 처리하였음
"""
while True:
    final_page = int(input())
    if final_page:
        pages = input().split(',')
        printing_pages = set()
        for page in pages:
            low, *high = map(int, page.split('-'))
            if low < 1:
                low = 1
            if high:
                high = high[0] if high[0] <= final_page else final_page
                if low <= high:
                    printing_pages.update(range(low, high + 1))
            elif low <= final_page:
                printing_pages.add(low)
        print(len(printing_pages))
    else:
        break