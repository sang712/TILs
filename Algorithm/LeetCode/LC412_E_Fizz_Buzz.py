'''
구현하였음
5의 배수의 경우 5로 직접 나누는 것보다 10으로 나눠서 나머지가 0 또는 5인지 확인하는 것이 더 빨랐음
대신 3의 배수의 경우 자릿수의 합이 3의 배수임을 이용하는 것은 빨라지지 않음
'''
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range(1, n+1):
            temp = ''
            if i % 3 == 0: temp += "Fizz"
            if i % 10 == 0 or i % 10 == 5: temp += "Buzz"
            if temp == '': temp = str(i)
            answer.append(temp)
        return answer