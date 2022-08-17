import requests
print("moshe")
try:
    f = int(input("enter number: "))
    r = 5 /0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("somthing went wrong , here is why")
    print(e.args)
print("haim")
