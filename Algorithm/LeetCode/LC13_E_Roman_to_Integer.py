class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        length = len(s) -1
        while length >= 0:
            roman = s[length]
            sub_roman = s[length-1] if length > 0 else 'None'
            if roman == 'I':
                num += 1
            elif roman == 'V':
                if sub_roman == 'I':
                    num += 4
                    length -= 1
                else: num += 5
            elif roman == 'X':
                if sub_roman == 'I':
                    num += 9
                    length -= 1
                else: num += 10
            elif roman == 'L':
                if sub_roman == 'X':
                    num += 40
                    length -= 1
                else: num += 50
            elif roman == 'C':
                if sub_roman == 'X':
                    num += 90
                    length -= 1
                else: num += 100
            elif roman == 'D':
                if sub_roman == 'C':
                    num += 400
                    length -= 1
                else: num += 500
            elif roman == 'M':
                if sub_roman == 'C':
                    num += 900
                    length -= 1
                else: num += 1000
            length -= 1
        return num