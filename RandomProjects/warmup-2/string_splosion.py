# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

test_string = "Code"


def string_splosion(s):
    new_str = ""
    counter = 0

    for i in range(len(test_string) + 1):
        new_str = new_str + test_string[:counter]
        counter += 1
    return new_str


print(string_splosion(test_string))
