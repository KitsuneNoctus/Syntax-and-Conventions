'''
Problem 4:
Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.

Restate the problem:
Given a string of text and the number k, find the number of words that appear multiple times in the text, up to the number k in the number of words. Return them in an array of decreasing order.

I have, I will, I want. It is I that will have the item. I want it.
k = 3
answer = [“I”, “have”, “will”]

Pseudo:
Essentially to make a dictogram - 
function takes in a string
converts to a list, stripped of spaces and punctuation
go through list and add to dictionary
check if in the dictionary
add one to the count value of the dictionary key
it not
add to dictionary with count 1
Organize the dictionary by value amounts - hopefully in descending order
add the key values to a list via k
return list
'''

def frequent_words(string, k):
    ''' Code complexity is intense'''
    word_dict = {}
    some_list = []
    return_list = []
    # word_list = [line.strip() for line in string]
    # word_list = string.strip()
    # Creating a list of the words in the string
    word_list = string.split()
   
    if word_list is not None:
        # if the list has values, add the words to a dictionary and keep track of the 
        # Number of times a word appears
        for word in word_list:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
    # Sorts the dictionary by by values in descending order            
    sorted_dict = sorted(word_dict.items(), key=lambda item: item[1], reverse = True)

    for object in sorted_dict:
        some_list.append(object)
    for i in range(0,k):
        return_list.append(some_list[i])
    
    return return_list

print(frequent_words("I have not seen them in a while. I have not seen them for a mile. I have not seen them over there. I have not seen them anywhere.", 6))
print(frequent_words("I have not seen them in a while. I have not seen them for a mile. I have not seen them over there. I have not seen them anywhere.", 8))
print(frequent_words("Running away. away. away. away", 1))