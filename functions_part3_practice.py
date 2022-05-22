# accepts any number of named arguments
# prints them in the pattern key : value one at a time
def name_args(**kwargs):
    for x, y in kwargs.items():
        print(x, ":", y)

#name_args(name="Lisa", car="honda")


# return true if all elements in an iterable are true
def all_true(x):
    x = all(x)
    print(x)

# expect True
true = [True, True, True]
#all_true(true)

empty = []
#all_true(empty)

# expect False
false = [True, False, True]
#all_true(false)


# one true returns true if one element is true
def one_true(x):
    x = any(x)
    print(x)

# expect False
false = [False, False, False]
#one_true(false)

empty = []
#one_true(empty)

# expect False
true = [False, False, True]
#one_true(true)


# Uses recursion to find the factorial of an integer
def recursive_factorial(num):
    if num == 1:
        return 1
    
    else:
        return (num * recursive_factorial(num-1))

#print(recursive_factorial(4))


# Recursively removes all adjacent duplicate letters from a string
def recursive_deduplicate(str):
    if len(str) < 2:
        return str
    if str[0] != str[1]:
        return str[0] + recursive_deduplicate(str[1:])
    return recursive_deduplicate(str[1:])

dup_input = ("aabbccdd")
#print(recursive_deduplicate(dup_input))

dup_input1 = ("aa")
#print(recursive_deduplicate(dup_input1))


# Uses recursion to reverse a string
def recursive_reverse(string):
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

rev_input = ("hello")
print(recursive_reverse(rev_input))