# if (3>4):
#     print("True Statement")    
# else:
#     print("False Statement")

#create a function
# def print_x_times(parameter="loop", loop_amount=5):
#     counter = 0
#     while counter < loop_amount:
#         print(counter,parameter)
#         counter += 1
#     return loop_amount

# call the function
# test = print_x_times("Something", 4)
# print(test)

#Hypotenuse Calculator
# print("Hypotenuse Calculator")
# def hypotenuse_calculator(length = 1, breadth = 1):
#     hypotenuse = float((length**2 + pow(breadth, 2))**(0.5))
#     print("The hypotenuse is : ", hypotenuse)
#     return round(hypotenuse,1)

# print(hypotenuse_calculator(length = 5, breadth = 4))

#Exercise 4
def shouter_function(output_string="Hello", repetition_number = 1):
    print(list(range(repetition_number)))
    if repetition_number < 10:
        for i in range(repetition_number):
            print(output_string.upper())
    else:
        print("You are too loud!")
    return "Done!"

#call the function
status = shouter_function("Hello World",3)
print(status)