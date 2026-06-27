#Documentation  Strings
total=0
def sum_of_numbers(a, b=300):
       """
       This is the sum of two numbers...
       :param a:
       :param b:
       :return:
       """
       print(a)
       print(b)
       # Local Variable
       total = (a + b)
       print("From inside", total)
       return  total

n = sum_of_numbers(500,500)
print("From Outside",total)

#
# #Default Arguments
# total=0
# def sum_of_numbers(a, b=300):
#        print(a)
#        print(b)
#        # Local Variable
#        total = (a + b)
#        print("From inside", total)
#        return  total
#
# n = sum_of_numbers(500,500)
# print("From Outside",total)

# #Global Variable
# total=0
# def sum_of_numbers(a, b):
#        print(a)
#        print(b)
#        # Local Variable
#        total = (a + b)
#        print("From inside", total)
#        return  total
#
# n = sum_of_numbers(10,20)
# print("From Outside",total)




# Positional Arguments
# result = sum_of_numbers(10, 20)
# print(result)

# Named Arguments
# result = sum_of_numbers(b=10, a= 20)
# print(result)


# tom =[1,2,3,4,5,6,7,8,9]
# joe=[100,200]
#
# def fun_get_total(exp):
#     total_amount = 0
#     for item in exp:
#         total_amount = total_amount + item
#     return total_amount
#
# total_of_tom = fun_get_total(tom)
# print(total_of_tom)
# print("#*************************************")
# total_of_joe = fun_get_total(joe)
# print(total_of_joe)
#



# total=0
# for item in tom:
#     total+=item
#     print(total)
#
# total=0
# for item in joe:
#     total+=item
#     print(total)







