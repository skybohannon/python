# jabba = open("sample.txt",'r')
# for line in jabba:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabba.close()

# with open("sample.txt",'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

with open("sample.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')


