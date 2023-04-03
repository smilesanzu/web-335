#author: Janis Gonzalez
#title: gonzalez_calculator.py
#date: 04/02/2023
#description: python variables and functions

#adds two variables
def add(a,b):
    #returns total
    return a + b

#subtracts two variables
def subtract(a,b):
    #returns total
    return a - b

#divides two variables
def divide(a,b):
    #returns total
    return a / b

#multiplies two variables
def multiply(a,b):
    #returns total
    return a * b

#testing each function
add1 = 3
add2 = 4

sub1 = 12
sub2 = 4

div1 = 6
div2 = 2

multi1 = 6
multi2 = 4

#string for the results
add_total = "{} + {} is {}".format(add1, add2, add(add1, add2))
sub_total = "{} - {} is {}".format(sub1, sub2, subtract(sub1, sub2))
div_total = "{} / {} is {}".format(div1, div2, divide(div1, div2))
multi_total = "{} * {} is {}".format(multi1, multi2, multiply(multi1, multi2))

#results printed
print(add_total)
print(sub_total)
print(div_total)
print(multi_total)