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

# List Comprehensions
simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a','b','c') if j == 'a']
print(simple_list)

# lambda functions
def double_value(num):
    return num*2
print(double_value(10))

