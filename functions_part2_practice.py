# takes any number of args
# prints them one at a time
def arb_args (*nums):
    for x in nums:
        print(x)

#arb_args(1,2,3,4)

# takes in two integers
# two nested functions to perform separate math operations using the integers
# the result of both nested functions should be added together and printed
def inner_func (num1, num2):
    def add (num1, num2):
        return num1 + num2
    def multiply (num1, num2):
        return num1 * num2
    print(add(num1,num2) + multiply(num1,num2))

#inner_func(2,3)

# takes in two strings: student name and lunch preference
# prints both strings, but if lunch preference is not given mystery meat s/b printed
def lunch_lady(student_name, lunch_pref="Mystery meat"):
    print("My name is: " + student_name)
    print("My preferred lunch is: " + lunch_pref)

#lunch_lady("Debbie")
#lunch_lady("Lisa", "salad")

# sum and product
def sum_n_product(int1, int2):
    sum = int1 + int2
    product = int1 * int2
    print("The sum of these numbers is: ", sum)
    print("The product of these numbers is: ", product)

#sum_n_product(2, 2)

# alias is just declaring another function

# 



def arb_longest_string(lst):
    return max(lst, key=len)

#print(arb_longest_string(["lisa","miguel","landon","jeremy","don"]))
