"""
문자열로 처리를 하면 처리속도가 너무 느릴 것 같아 리스트에 담아서 풀이하였음
우선 A와 B의 알파벳을 숫자로 변환해 리스트에 합쳐서 저장하였고
while문을 돌면서 숫자를 더하고 마지막 수는 없애는 방식으로 단계를 진행하였음
마지막에는 10의 자리에 0이 남아도 출력될 수 있게 자리수 별로 출력을 하였음
"""
alphabets = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3,
            'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2,
            'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1, 
            'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 
            'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

A = input()
B = input()
AB = []
for i in range(len(A)):
    AB.append(alphabets[A[i]])
    AB.append(alphabets[B[i]])
    
while len(AB) > 2:
    for i in range(1, len(AB)):
        AB[i - 1] = (AB[i - 1] + AB[i]) % 10
    AB.pop()
    
print(*AB, sep='')