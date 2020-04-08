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

def find_dup(array):
        dup_array = []
        for number in array:
            if number in array:
                return True
            else:
                dup_array.append(number)
        #Returning false if no dup is found
        return False


print(find_dup(list1))
