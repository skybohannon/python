import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 Dream"
    # bike["color"] = "red"
    # bike["engine_size"] = 250

    del bike["engin_size"]

    for key in bike:
        print(key)

    print("=" * 40)

    print(bike["engine_size"])
    print(bike["color"])