def grade_class(perc):
    for num in range(len(perc)):
        if float(perc[num]) < 60:
            print("F")
        elif float(perc[num]) >= 93 and float(perc[num]) <= 100:
            print("A")
        elif float(perc[num]) >= 90 and float(perc[num]) <= 92.99:
            print("A-")
        elif float(perc[num]) >= 87 and float(perc[num]) <= 89.99:
            print("B+")
        elif float(perc[num]) >= 83 and float(perc[num]) <= 86.99:
            print("B")
        elif float(perc[num]) >= 80 and float(perc[num]) <= 82.99:
            print("B-")
        elif float(perc[num]) >= 77 and float(perc[num]) <= 79.99:
            print("C+")
        elif float(perc[num]) >= 73 and float(perc[num]) <= 76.99:
            print("C")
        elif float(perc[num]) >= 70 and float(perc[num]) <= 72.99:
            print("C-")
        elif float(perc[num]) >= 67 and float(perc[num]) <= 69.99:
            print("D+")
        elif float(perc[num]) >= 63 and float(perc[num]) <= 66.99:
            print("D")
        elif float(perc[num]) >= 60 and float(perc[num]) <= 62.99:
            print("D-")

list = ['87.01', '61.99', '95.94', '80.94', '91.34']

grade_class(list)
