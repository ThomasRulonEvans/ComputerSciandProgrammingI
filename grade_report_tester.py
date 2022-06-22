#!/usr/bin/env python3

import traceback

import grades

def get_t_f_str(check):
    return ("\033[1;32m" if check else "\033[1;31m") + str(check)

def test_get_class_percents():
    print("\033[1;30mStarting Test: \033[1;34mget_class_percents")
    num_students_tests = [42]
    for num_students in num_students_tests:
        gcp_results = grades.get_class_percents(num_students)
        is_list = type(gcp_results) == type(list())
        correct_len = len(gcp_results) == num_students
        
        grades_are_floating_point = True
        grades_are_valid = True
        for grade in gcp_results:
            if not (50 <= grade <= 100):
                grades_are_valid = False
            if type(grade) != type(float()):
                grades_are_floating_point = False

        print("\033[0;0mTest case: {}".format(num_students))
        print("\033[0;0m\tReturn value was a list: {}".format(get_t_f_str(is_list)))
        print("\033[0;0m\tReturn value was correct length: {}".format(get_t_f_str(correct_len)))
        print("\033[0;0m\tList contained only floating point numbers: {}".format(
                get_t_f_str(grades_are_floating_point)))
        print("\033[0;0m\tGrades were between 50 and 100 inclusive: \033[1;31m{}".format(
                get_t_f_str(grades_are_valid)))

def test_grade_class():
    print("\033[1;30mStarting Test: \033[1;34mgrade_class")
    test_grades = [0,  59.9, 60.0, 65, 69.9,  73, 81.3,   87, 92.9,  97]
    test_expect = ["F", "F", "D-", "D", "D+", "C", "B-", "B+", "A-", "A"]

    grade_result = grades.grade_class(test_grades)
    correct_len = len(grade_result) == len(test_grades)
    print("\033[0;0mOutput list length was correct: {}".format(get_t_f_str(correct_len)))

    for grade_index, grade_pair in enumerate(grade_result):
        grade_percent, grade_letter = grade_pair
        correct_grade = grade_letter == test_expect[grade_index]
        print("\033[0;0mTest case: {}".format(test_grades[grade_index]))
        print("\033[0;0m\tExpected grade_percent: \033[1;30m{} \033[0;0mactual: \033[1;30m{}".format(
                test_grades[grade_index], test_grades[grade_index]))
        print("\033[0;0m\tGrade conversion was correct: \033[1;30m{}".format(get_t_f_str(correct_grade)))
        print("\033[0;0m\tgrade_class returned an: \033[1;30m{} \033[0;0mexpected an: \033[1;30m{}".format(
                grade_letter, test_expect[grade_index]))

def test_pretty_print():
    print("\033[1;30mStarting Test: \033[1;34mpretty_print")

    test_grades = [0,  59.9, 60.0, 69.9,  73, 81.3,   87, 92.9,  97]
    test_letter = ["F", "F", "D-", "D+", "C", "B-", "B+", "A-", "A"]
    grade_data = list(zip(test_grades, test_letter))

    class_name = "Fundamentals of fundamentals courses"
    min_grade = min(test_grades)
    max_grade = max(test_grades)
    avg_grade = sum(test_grades) / len(grade_data)

    print("\033[0;0mTest case grade data: \033[1;30m{}".format(grade_data))
    print("\033[0;0mTest case class name: \033[1;30m{}".format(class_name))
    print("\033[0;0mOutput should look very similar to what's seen in the example IO.")
    print("\033[0;0mNumber of grades should be: \033[1;30m{}".format(len(grade_data)))
    print("\033[0;0mMinimum grade should be: \033[1;30m{:.2f}".format(min_grade))
    print("\033[0;0mMaximum grade should be: \033[1;30m{:.2f}".format(max_grade))
    print("\033[0;0mAverage grade should be: \033[1;30m{:.2f}".format(avg_grade))
    print("\033[1;30m\t\t\toutput:\033[0;0m ")
    grades.pretty_print(grade_data, class_name)

def run_tests():
    try:
        test_get_class_percents()
    except Exception:
        traceback.print_exc()

    print("\033[1;0m" + "-"*40)

    try:
        test_grade_class()
    except Exception:
        traceback.print_exc()

    print("\033[1;0m" + "-"*40)

    try:
        test_pretty_print()
    except Exception:
        traceback.print_exc()

    print("\033[1;0m" + "-"*40)


if __name__ == "__main__":
    run_tests()
