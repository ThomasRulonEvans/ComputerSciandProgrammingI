import roman_numerals

num1 = int(input("Pick a number between 1 and 5."))
num2 = int(input("Pick another number between 1 and 5."))
sum = 0
if roman_numerals.check_extents(1, 5, num1) and roman_numerals.check_extents(1, 5, num2):
    sum = num1 + num2
if sum != 0:
    print(roman_numerals.get_roman_numeral(sum))
else:
    print("Invalid inputs")
