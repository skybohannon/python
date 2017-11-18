# """
# Define a function postalValidate(S) which first checks if S represents
# a postal code (Canadian) which is valid:
#     first, delete all spaces;
#     the remainder must be of the form L#L#L# where L are letters
#     (in either lower or upper case) and # are numbers.
#
# If S is not a valid postal code, return the boolean False.
# If S is valid, return a version of the same postal code in the nice format
# L#L#L# where each L is capital.
# Use the following methods to do this exercise:
# str.replace(), str.isalpha(), str.isdigit(), and str.upper()
# """
#
#
# def postalValidate(S):
#     """ Return False if S is not a valid postal code.
#     If S is valid, return it in the format L#L#L# where each L is capital.
#
#     >>> postalValidate(' d3 L3 T3')
#     >>> 'D3L3T3'

postal_code = " d3 L3 T3"


def postal_validate(postal):
    postal = postal.replace(" ", "").upper()

    if len(postal) == 6:
        for i in range(len(postal)):
            if i % 2 == 0:
                # even has to be letter
                if not (postal[i].isalpha()):
                    return False
            else:
                # odd has to be number
                if not (postal[i].isdigit()):
                    return False
    else:
        return False

    return postal


print(postal_validate(postal_code))
