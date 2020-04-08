'''
Problem 1:
Given list of any length of numbers, determine if there are any duplicate numbers within

list1 = [1,2,3,4,5,5,6,7,8,9,]
return True

list2 = [9,4,2,3,4,8,10,11]
return True

list3 = [2,3,4,5,6,7,8,9,0]
return false

Pseudo:
Function of find duplicates( takes in array)
    empty array start
    for number in the array:
        if the number id in the array:
            return True
        else:
            append number to empty array
    return False

'''
list1 = [1,2,3,4,5,5,6,7,8,9,]
list2 = [9,4,2,3,4,8,10,11]
list3 = [2,3,4,5,6,7,8,9,0]

def find_dup(array):
    '''
    This turned out incorrect as it always returned true because it would
    just check that the number was in the array
    Should be (as is now fixed), that it checks if it in the dupe array
    '''

    # This is a brute force method with time complexity of 0(n^2)
    dupe_array = []
    for number in array:
        if number in dupe_array:
            return True
        else:
            dupe_array.append(number)
    #Returning false if no dup is found
    return False

print(find_dup(list1))
print(find_dup(list2))
print(find_dup(list3))
