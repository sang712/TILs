'''
9, 5, 4 로 시작하는 수는 한번만 나오므로 if, elif 분기로 가지를 쳐주었음
104ms -> 73ms
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        while num >= 1000:
            ans += 'M'
            num -= 1000
        if num >= 900:
            ans += 'CM'
            num -= 900
        elif num >= 500:
            ans += 'D'
            num -= 500
        elif num >= 400:
            ans += 'CD'
            num -= 400
        while num >= 100:
            ans += 'C'
            num -= 100
        if num >= 90:
            ans += 'XC'
            num -= 90
        elif num >= 50:
            ans += 'L'
            num -= 50
        elif num >= 40:
            ans += 'XL'
            num -= 40
        while num >= 10:
            ans += 'X'
            num -= 10
        if num >= 9:
            ans += 'IX'
            num -= 9
        elif num >= 5:
            ans += 'V'
            num -= 5
        elif num >= 4:
            ans += 'IV'
            num -= 4
        while num >= 1:
            ans += 'I'
            num -= 1
        return ans