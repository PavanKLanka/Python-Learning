# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
try:
    max_input_number = int(input("Enter Max Number here: "))
    staring_odd_number = 1
    odd_numbers_list = []
    while staring_odd_number <= max_input_number:
        if staring_odd_number % 2 != 0:
            odd_numbers_list.append(staring_odd_number)
            staring_odd_number = 1 + staring_odd_number
        else:
            staring_odd_number = 1 + staring_odd_number
            continue
    print(odd_numbers_list)
except ValueError as e:
    print(type(e).__name__)
