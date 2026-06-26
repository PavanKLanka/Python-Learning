exp = [2340, 2500, 2100, 3100, 2980]
# total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]'
# total=0
# for item in exp:
#     total = total + item
# print(total)
# ***************************************
# total=0
# for i in range(len(exp)):
#     print(i+1, exp[i])
#     total = total + exp[i]
#     print(total)
# ***************************************
# for i in range(5):
#     print(i)
# ***************************************
# for i in range(1,10):
#         print(i)
# ***************************************
# for i in range(1,10,2):
#     print(i)
# ***************************************
# key_location = "chair"
# locations=["garage","chair","area","offiice"]
# for i in locations:
#     if i==key_location:
#         print("found in chair")
#         break
#     else:
#         print("not found in "+i)
#         continue
# ***************************************
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i * i)
