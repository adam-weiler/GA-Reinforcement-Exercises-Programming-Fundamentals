#Exercise 1

all_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'] #List stores all letter grades.

def display_grade(num_grade, position): #Returns percent grade and letter grade.
    return (f'With a grade of {num_grade}, you get an {all_grades[position]}.')


def get_letter_grade(num_grade): #Based on user input, calls display_grade with appropriate reference for the list.
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
        return ('That is an invalid selection.')

def ask_for_grade(): #Asks user for their grade as a percentage.
    print('What is your grade percentage?')
    grade_percentage = float(input())

    return get_letter_grade(grade_percentage)


print(ask_for_grade())