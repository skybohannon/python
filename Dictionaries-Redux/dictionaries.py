fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit, grown in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

# orderedKeys = sorted(list(fruit.keys()))
# print(orderedKeys)
# for f in orderedKeys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for f in fruit:
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print("-" * 40)

# fruitKeys = fruit.keys()
# print(fruitKeys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruitKeys)
#
# print(fruit.keys())
# print(fruit.values())

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))