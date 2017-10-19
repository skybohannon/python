import  shelve

books = shelve.open("books")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beansOnToast": ["beans", "bread"],
                    "scrambledEggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}

books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambledEggs"])
# print(books["maintenance"]["loose"])
books.close()