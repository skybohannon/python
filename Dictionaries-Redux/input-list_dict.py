fruit = {"apple": "one uh dem red fruit",
         "banana": "a long, yellow fruit",
         "grape": "little and round, come in bunches",
         "pineapple": "the best fruit in existence"}

print(fruit)
while True:
    dictKey = input("Please enter a fruit: ")
    if dictKey == "quit":
        break
    if dictKey in fruit:
        description = fruit.get(dictKey)
        print(description)
    else:
        print("We don't have a " + dictKey)