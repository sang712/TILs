# Read input for birth date and reference date
birth_year, birth_month, birth_day = map(int, input().split())
ref_year, ref_month, ref_day = map(int, input().split())

# Calculate Man Age (Korean Age)
if birth_month < ref_month:
    man_age = ref_year - birth_year
elif birth_month == ref_month and birth_day <= ref_day:
    man_age = ref_year - birth_year
else:
    man_age = ref_year - birth_year - 1

# Calculate korean Age (Korean Age Counting)
se_age = ref_year - birth_year + 1

# Calculate Ye Age (International Age)
ye_age = ref_year - birth_year 

# Output the results
print(man_age)
print(se_age)
print(ye_age)
