# def get_longest_name(a_list):
#     """ Return '******' if the input list is [], [''], or a list containing
#         names of equal length.
#         Else, return the name that is greater in length than any other name
#         in the list.
#
#     >>> get_longest_name(["Candide", "Jessie", "Kath", "Amity", "Raeanne"])
#     >>> '******'
#     >>> get_longest_name(["Jessie", "Kath", "Amity", "Raeanne"])
#     >>> '******'
#     >>> get_longest_name(["Jessie", "Kath", "Amity"])
#     >>> 'Jessie'
#     """

name_list = ["Candice", "Jessie", "Kath", "Amity", "Raeanneo"]
def longest_name(lst):

    d = dict.fromkeys(set(name_list), 0)

    if name_list == [] or name_list == ['']:
        return("******")

    else:
        for name in name_list:
            d[name] += len(name)

    # pairs = d.items()
    # print(pairs)
    # for pair in pairs:
    #
    #     if check_dupe == pair[1]:
    #         return("******")
    #     check_dupe = pair[1]

    return(max(d, key=d.get))


print(longest_name(name_list))
