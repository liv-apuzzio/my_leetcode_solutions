def findRestaurant(list1, list2):
    dict1 = dict()
    answer = []
    for i in range(0, len(list1)):
        if list1[i] in list2:
            dict1.update({list1[i]: (list1.index(list1[i]) + list2.index(list1[i]))})
    for key, value in dict1.items():
        if min(dict1.values()) == value:
            answer.append(key)
    return answer