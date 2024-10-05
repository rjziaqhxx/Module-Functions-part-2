def func(list, num_remove):
    original_length = len(list)
    while num_remove in list:
        list.remove(num_remove) 
    return original_length - len(list)

numbers = [1,2,3,4,5,6,7,8,2]
print(func(numbers, 2),'updated list - ' ,numbers)