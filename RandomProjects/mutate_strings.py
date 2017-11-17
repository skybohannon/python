# # Define a function that does this:
# # Given a list of strings, with each string having a student’s name and
# # their grades, mutate the input list so the original string positions are
# # replaced with their average grades. The function doesn’t need an explicit
# # return statement.
# reports = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']
# get_averages(reports)
# print(reports)
# # [74.0, 65.0, 98.0]

reports = ['Anna, 50, 92, 80', 'Bill, 60, 70', 'Cal, 98.5, 100, 95.5, 98']


def get_averages(lst):
    listcount = 0
    for person in reports:
        person_split = person.split(", ")
        average = 0
        counter = 0

        for grade in person_split[1:]:
            counter += 1
            average += float(grade)

        average = average/counter
        reports[listcount] = average
        listcount += 1


get_averages(reports)
print(reports)
