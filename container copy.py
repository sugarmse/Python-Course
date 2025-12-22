#container setup
a_tuple = (1, 2, 3, "a string")
a_list = [1, 2, 3, "a string", 2]
a_list.append("another word")
a_set = {1, 2, 3, 4, 4} # sets value is unique
# print(a_tuple)
# print(a_list)
# print(a_set)
# print(list(set(a_list)))  # converting list to set to remove duplicates
a_dictionary = {'key': 'value', 123: [1, 2, 3]}

#how to access values
user_list = ['Alex', 'John', 'Mary', 'Sam']
# print(user_list[1])
# print(user_list[0:3:2])  #slicing [start: end: step]
# print(a_dictionary[123])

#exercise 3
exercise_list = [1,2,3,4,5,6,7,8,9,10]
print(exercise_list[-3:0:-2])