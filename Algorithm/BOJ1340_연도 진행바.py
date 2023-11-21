"""
1월 1일은 0% 진행되었다는 것을 고려해야 함
"""
month_to_digit = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                  'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
month_to_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day, year, time = input().split()
current_days = int(day.strip(',')) - 1
for m in range(month_to_digit[month]):
    current_days += month_to_days[m]

whole_year = 365
if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100):
    whole_year += 1
    if month_to_digit[month] > 2: current_days += 1

whole_year_to_time = whole_year * 1440
current_time = current_days * 1440 + int(time[:2]) * 60 + int(time[3:])

print(current_time / whole_year_to_time * 100)