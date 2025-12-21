#f strings
user_name = 'Bob'
user_age = 10
user_information = f'{user_name} is {user_age} years old.'
bad_approach = user_name + ' is ' + str(user_age) + ' years old.'  #bad approach
print(user_information)

# Single line if statements
# user_age = 20
# user_status = "Adult" if user_age >18 else "Child"
# print(user_status)
print(f"{user_name} is an {'Adult' if user_age >18 else 'Child'}")