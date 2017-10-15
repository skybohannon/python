fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit, grown in bunches",
         "lime": "a sour, green citrus fruit",
         }

# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# # del fruit["lemon"]
# # fruit.clear() #clear entire dictionary
# # print(fruit)
#
# print(fruit["tomato"])

print(fruit)
while True:
    dictKey = input("Please enter a fruit: ")
    if dictKey == "quit":
        break
    if dictKey in fruit:
        description = fruit.get(dictKey)
        print(description)
    else:
        print("Don't have a " + dictKey)