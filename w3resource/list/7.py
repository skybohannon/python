# 7. Write a Python program to remove duplicates from a list.

dupes = []
uniques = []

def remove_dupes(l):
    for x in l:
        if x not in dupes:
            uniques.append(x)
            dupes.append(x)
    return "Unique numbers are: " + str(sorted(dupes))

print(remove_dupes([10,20,30,20,10,50,60,40,80,50,40]))
