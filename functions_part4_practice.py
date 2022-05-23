# define a function to find the maximum of three numbers
def max_num(x):
    print("The largest number is: ", max(x))

list = [10, 20, 40, 15]
max_num(list)

# define a function to multiply all the numbers in a list
def mult_list(num_list):
    # to multiply each number one at a time
    result = 1
    for x in num_list:
        result = result * x
    return result
    
list = [10, 20, 30]
print(mult_list(list))

# define a function to reverse a string
def rev_string(str):
    if len(str) == 0:
        return str
    else:
        return rev_string(str[1:]) + str[0]

print(rev_string("reverse"))


# define a function to check whether a number falls in a given range
def num_within(num, beg, end):
    if num >= beg and num <= end:
        return True
    else: 
        return False

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

# define a function that prints out the first n rows of Pascal's triangle
def pascal(x):
    switcher = {
       1: "1",
       2: "1 \n1 1",
       3: "1 \n1 1\n1 2 1",
       4: "1 \n1 1\n1 2 1\n1 3 3 1",
       5: "1 \n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1"
    }
    return switcher.get(x, "Invalid number")
    

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))