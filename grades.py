import random

number_students = int(input("Number of students"))


def get_class_percents(students):
    percents = []
    for i in range(students):
        origpercent = " %#.2f " % random.uniform(50,100.01)
        percents.append(origpercent)
    return percents

def grade_class(perc):
    combined = []
    for num in range(len(perc)):
        if float(perc[num]) < 60:
            combined.append([float(perc[num]),"F"])

        elif float(perc[num]) >= 93 and float(perc[num]) <= 100:
            combined.append([float(perc[num]),"A"])

        elif float(perc[num]) >= 90 and float(perc[num]) <= 92.99:
            combined.append([float(perc[num]),"A-"])

        elif float(perc[num]) >= 87 and float(perc[num]) <= 89.99:
            combined.append([float(perc[num]),"B+"])

        elif float(perc[num]) >= 83 and float(perc[num]) <= 86.99:
            combined.append([float(perc[num]),"B"])

        elif float(perc[num]) >= 80 and float(perc[num]) <= 82.99:
            combined.append([float(perc[num]),"B-"])

        elif float(perc[num]) >= 77 and float(perc[num]) <= 79.99:
            combined.append([float(perc[num]),"C+"])

        elif float(perc[num]) >= 73 and float(perc[num]) <= 76.99:
            combined.append([float(perc[num]),"C"])

        elif float(perc[num]) >= 70 and float(perc[num]) <= 72.99:
            combined.append([float(perc[num]),"C-"])

        elif float(perc[num]) >= 67 and float(perc[num]) <= 69.99:
            combined.append([float(perc[num]),"D+"])

        elif float(perc[num]) >= 63 and float(perc[num]) <= 66.99:
            combined.append([float(perc[num]),"D"])

        elif float(perc[num]) >= 60 and float(perc[num]) <= 62.99:
            combined.append([float(perc[num]),"D-"])
    return combined

def pretty_print(combo,name):
    print(name  + '\n' + "Grades for a class that doesn't exist I guess?"+ '\n' + "  Numeric Grade (%)     Letter Grade")
    for i in range(len(combo)):
        print("    "," %#.2f " % combo[i][0], "                 ", combo[i][1])
    print("Total Grades:", number_students)
    print("Minimum Grade:", min(percent_grades))
    print("Maximum Grade:", max(percent_grades))
    added = 0
    for i in range(len(percent_grades)):
        added += float(percent_grades[i])
    average = added / len(percent_grades)
    print("Average Grade:", " %#.2f " % average)


percent_grades = get_class_percents(number_students)
both_grades = grade_class(percent_grades)
name = "class name"

pretty_print(both_grades,name)
