'''
오탈자를 찾는 것이 가장 큰 문제였음
forty 와 fourteen이 다르게 쓰인다는 점을 알게 되었음
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        commas = 0
        comma_units = ['', 'Thousand ', 'Million ', 'Billion ']
        ten_units = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
        one_unit = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ']
        output = ''
        if num == 0:
            return 'Zero'
        
        while num:
            ans = ''
            temp_num = num % 1000
            h_digit = temp_num // 100
            if h_digit > 0:
                ans += one_unit[h_digit] + 'Hundred '
            temp_num %= 100
            if 10 <= temp_num <= 19:
                ans += ten_units[temp_num]
            else:
                t_digit = temp_num // 10
                o_digit = temp_num % 10
                ans += ten_units[t_digit] + one_unit[o_digit]
            num //= 1000
            output = ans + comma_units[commas] + output if ans else output
            commas += 1
        return output.rstrip()