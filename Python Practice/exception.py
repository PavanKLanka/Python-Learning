x=input("enter your age:")
y=input("enter your friend age:")
try:
    z = int(x) / int(y)
    print("z is:", z)
except ZeroDivisionError as e:
    z=None
    print(e)
except Exception as e:
    print(type(e).__name__)

