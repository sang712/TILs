'''
이미지를 왼위, 오위, 왼아, 왼오의 네 칸으로 나누어
2*2 크기가 될 때까지 재귀를 사용하는 방법을 이용하였음

재채점 추가: N이 1일 경우를 고려하지 않고 temp가 4개일 경우만 생각하여
image가 1이나 0일 때 괄호 없이 출력되는 경우를 빠뜨렸음
해당 부분 추가하였음
'''
N = int(input())

image_ = []
for _ in range(N):
    image_.append(input())

def compressing(sr, er, sc, ec):
    '''
    압축 함수
        Args:
            sr (int): 시작 row 인덱스
            er (int): 끝 row 인덱스 +1
            sc (int): 시작 column 인덱스
            ec (int): 끝 column 인덱스 +1
        Returns:
            압축결과
    '''
    mr = int((sr + er)//2)
    mc = int((sc + ec)//2)
    
    temp = ''
    if er - sr == 1:
        temp = image_[sr]
        return temp
    elif er - sr == 2:
        for r in range(sr, er):
            temp += image_[r][sc:ec]
        temp = '(' + temp + ')'
        temp = temp.replace('(0000)', '0')
        return temp.replace('(1111)', '1')
    
    compressed = f'({compressing(sr, mr, sc, mc)}{compressing(sr, mr, mc, ec)}{compressing(mr, er, sc, mc)}{compressing(mr, er, mc, ec)})'
    compressed = compressed.replace('(0000)', '0', 4)
    compressed = compressed.replace('(1111)', '1', 4)
    return compressed

print(compressing(0, N, 0, N))