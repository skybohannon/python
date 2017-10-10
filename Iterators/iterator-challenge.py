# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

arsenal_11 = ["Cech", "Koscielny", "Mustafi", "Holding", "Kolasinac", "Bellerin", "Ramsey", "Xhaka", "Ozil", "Alexis", "Lacazette"]
teamIterator = iter(arsenal_11)

print("Arsenal starting 11:")
for player in range(0, len(arsenal_11)):
    nextPlayer = next(teamIterator)
    print(nextPlayer)

#easier way
for player in arsenal_11:
    print(player)