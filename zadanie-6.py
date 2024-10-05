def func(list, power):
    l = []
    for i in list:
        l.append(i ** power)
    return l

nums = [1,2,3,4]
print(func(nums,3))