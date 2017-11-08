# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

gradeList = [['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70], ['S-Bo', 70, 83, 69, 95]]


def averages(lst):
    new_list = []
    for student in lst:
        total_score = 0
        student_list = []
        student_list.append(student[0])

        grade_list = student[1:]

        for grade in grade_list:
            total_score = total_score + grade

        grade_count = len(grade_list)
        average_score = total_score / grade_count
        student_list.append(average_score)
        new_list.append(student_list)

    return new_list


averageList = averages(gradeList)
for student in averageList:
    print("{}: {}".format(student[0], student[1]))


# Processor: Intel Core i5-2520M @ 3.20GHz (4 Cores), Motherboard: LENOVO 4180W59,
# Chipset: Intel 2nd Generation Core Family DRAM, Memory: 8192MB, Disk: 500GB TOSHIBA MQ01ACF0,
# Graphics: Intel Sandybridge Mobile 1536MB (1300MHz), Audio: Conexant CX20590,
# Network: Intel 82579LM Gigabit Connection + Intel Centrino Advanced-N 6205