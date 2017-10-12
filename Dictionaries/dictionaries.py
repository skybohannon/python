fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit", }

print(fruit)

# orderedKey = list(fruit.keys())
# orderedKey.sort()
# orderedKey = sorted(list(fruit.keys()))
# for f in orderedKey:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])
#
# fruitKeys = fruit.keys()
# print(fruitKeys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruitKeys)

print(fruit.items())
fTuple = tuple(fruit.items())
print(fTuple)

for snack in fTuple:
    item, description = snack
    print(item + " is " + description)

print(dict(fTuple))