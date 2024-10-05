def func(list1,list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1

a = [1,2,3,4]
b = [5,6,7,8]
print(func(a,b))