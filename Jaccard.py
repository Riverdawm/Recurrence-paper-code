def jaccard_coefficient(list1, list2):
    set1 = set(list1[1]) & set(list2[1])
    jaccard_value = len(set1) / (len(list1[1]) + len(list2[1]) - len(set1))
    print(jaccard_value)


list1 = [0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 77, 66]]
list2 = [5, [6, 3, 7, 9, 23, 56, 94, 2,5]]
jaccard_coefficient(list1, list2)
