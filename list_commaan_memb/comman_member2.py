def common_data(list1, list2):
    return any (elements in list2 for elements in list1)
list1=[10,20,30,40]
list2=[50,60,30,70]
print(common_data(list1, list2))
