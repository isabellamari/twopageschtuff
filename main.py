#float is a number with a decimal (ex. 4.0, 5.0, 0.4)
#integers are whole numbers(ex. 1, 2, 3, 4,)
#strings anything between the quotes tha twe print
#bool is a value of true or false; true or false statements
#when you start calling functions from other modules thats where you use the dot

import not_main

number0 =0
print(number0)

def function1():
    global number0
    number0 = 3
    print(number0)
    number0 = number0 + 1
    print(number0)

function1()
print(number0)

#me = not_main.random_stu(16,"smith","john",3.8, False)
#print(me)
#print("next year you are " , me[0])