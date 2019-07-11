#Exercise 1

all_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']

def display_grade(num_grade, position):
    return (f'With a grade of {num_grade}, you get an {all_grades[position]}.')


def get_letter_grade(num_grade):
    if (num_grade >= 97) and (num_grade <= 100):
        return display_grade(num_grade, 0)
    elif (num_grade >= 93) and (num_grade < 97):
        return display_grade(num_grade, 1)
    elif (num_grade >= 90) and (num_grade < 93):
        return display_grade(num_grade, 2)
    elif (num_grade >= 87) and (num_grade < 90):
        return display_grade(num_grade, 3)
    elif (num_grade >= 83) and (num_grade < 87):
        return display_grade(num_grade, 4)
    elif (num_grade >= 80) and (num_grade < 83):
        return display_grade(num_grade, 5)
    elif (num_grade >= 77) and (num_grade < 80):
        return display_grade(num_grade, 6)
    elif (num_grade >= 73) and (num_grade < 77):
        return display_grade(num_grade, 7)
    elif (num_grade >= 70) and (num_grade < 73):
        return display_grade(num_grade, 8)
    elif (num_grade >= 67) and (num_grade < 70):
        return display_grade(num_grade, 9)
    elif (num_grade >= 63) and (num_grade < 67):
        return display_grade(num_grade, 10)
    elif (num_grade >= 60) and (num_grade < 63):
        return display_grade(num_grade, 11)
    elif (num_grade >= 0) and (num_grade < 60):
        return display_grade(num_grade, 12)
    else:
        return ('That is an invalid selection')

def ask_for_grade():
    while(True):
        print('What is your grade percentage?')
        grade_percentage = input()

        if (grade_percentage.isnumeric() == True):
            break
        print('That is an invalid percent.')
    return(get_letter_grade(int(grade_percentage)))


ask_for_grade()


# print(get_letter_grade(100))
# print(get_letter_grade(97))
# print(get_letter_grade(96.9))
# print(get_letter_grade(93))
# print(get_letter_grade(92.9))
# print(get_letter_grade(90))
# print(get_letter_grade(89.9))
# print(get_letter_grade(87))
# print(get_letter_grade(86.9))
# print(get_letter_grade(83))
# print(get_letter_grade(82.9))
# print(get_letter_grade(80))
# print(get_letter_grade(79.9))
# print(get_letter_grade(77))
# print(get_letter_grade(76.9))
# print(get_letter_grade(73))
# print(get_letter_grade(72.9))
# print(get_letter_grade(70))
# print(get_letter_grade(69.9))
# print(get_letter_grade(67))
# print(get_letter_grade(66.9))
# print(get_letter_grade(63))
# print(get_letter_grade(62.9))
# print(get_letter_grade(60))
# print(get_letter_grade(59.9))
# print(get_letter_grade(59))
# print(get_letter_grade(58.9))
# print(get_letter_grade(0))
# print(get_letter_grade(-27))
# print(get_letter_grade('A string'))
