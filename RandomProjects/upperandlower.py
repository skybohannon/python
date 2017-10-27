def uplowcalc(sentence):

    d = {"UPPER": 0, "LOWER": 0}
    for c in sentence:
        if c.isupper():
            d["UPPER"] += 1
        elif c.islower():
            d["LOWER"] += 1
        else:
            pass

    print("There were {} upper case characters".format(d["UPPER"]))
    print("There were {} lower case characters".format(d["LOWER"]))

uplowcalc('The quick Brown Fox')