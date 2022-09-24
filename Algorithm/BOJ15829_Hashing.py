'''
제곱 연산이 오래걸릴 것 같아서 리스트를 추가했는데 속도 개선은 없었고 그냥 해도 될 것 같다
python이 아니라면 long 타입을 사용하여 오버플로우를 방지해야 한다
'''
L = int(input())
_string = input()

hash = 0
multiple_of_31 = [1]
for i in range(L):
    multiple_of_31.append(multiple_of_31[i]*31)
    hash += (ord(_string[i]) - 96) * (multiple_of_31[i])
    
print(hash%1234567891)

'''
20ms 빠른 코드
enumerate를 사용하였다!!

r=31
m=1234567891
n=int(input())
s=input()
print(sum((ord(c)-96)*r**i%m for i, c in enumerate(s))%m)
'''