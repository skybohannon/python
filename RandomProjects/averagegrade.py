# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

gradeList = [['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70], ['S-Bo', 70, 83, 69, 95]]


def averages(lst):
    new_list = []
    for student in lst:
        total_score = 0
        average_score = 0
        student_list = []

        student_list.append(student[0])
        grade_list = student[1:]

        for grade in grade_list:
            grade_count = len(grade_list)
            total_score = total_score + grade
            average_score = total_score / grade_count

        student_list.append(average_score)
        new_list.append(student_list)
    return new_list


print(averages(gradeList))
