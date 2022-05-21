# Hello function to print a greeting
# Accepts no args
# Has no return
def hello():
    print("Hello, how are you?")

hello()


# Pack function
# Accepts three args
# Returns a single list with the 3 ars
def pack(first_name, fav_city, fav_dish):
    pack_list = [first_name, fav_city, fav_dish]
    print(pack_list)

pack("Lisa", "Pasadena", "Greek Salad")

# Eat lunch function
# Accepts a list of any length
# Print a series of strings as follows:
# "First I eat (first list element)"
# "Next I eat (following list elements)" 
# "My lunchbox is empty" if the list is empty
def eat_lunch(lunch):
    # Checking for an empty list and printing accoringly
    if len(lunch) > 0:
        print("First I eat my " + lunch[0])
        # remove the first item so I can print the remaining items
        first_item = lunch[0]
        lunch.remove(first_item)
        # loop through to print remaining items
        for i in lunch:
            print("Next I eat my " + i)
    else:
        print("My lunchbox is empty")
    

# Scenario one        
lunch_list1 = ["Turkey Sandwich", "Chicken Soup", "Apple"]
eat_lunch(lunch_list1)

# Scenario two
lunch_list2 = []
eat_lunch(lunch_list2)
