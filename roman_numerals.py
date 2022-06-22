def check_extents(min,max,val):
    if val >= min and val <= max:
        return True
    else:
        return False
        print("Invalid inputs")

def get_roman_numeral(arabic_num):
    if arabic_num == 1:
        return "I"
    elif arabic_num == 2:
        return "II"
    elif arabic_num == 3:
        return "III"
    elif arabic_num == 4:
        return "IV"
    elif arabic_num == 5:
        return "V"
    elif arabic_num == 6:
        return "VI"
    elif arabic_num == 7:
        return "VII"
    elif arabic_num == 8:
        return "VIII"
    elif arabic_num == 9:
        return "IX"
    elif arabic_num == 10:
        return "X"
