# A
x = 4
y = 89

if x > y:
    print("x is bigger ")
else:
    print("y is smaller ")

# B
for i in range(5):
    print(i)


# C

rainbow = 3
if rainbow == 1:
    print("summer")
elif rainbow == 2:
    print("winter")
elif rainbow == 3:
    print("fall")
elif rainbow == 4:
    print("spring")

# D
count = 1
while count < 11:
    print(count)
    count = count+1
# the loop run 10 times and the last printed number will be 10

# E

me = {'age' : 22, 'last_name' : 'f', 'shekels' : 3.46, 'abroad' : 'false', 'apartment_num' : 15}

for i in me.items():
    print(i[0], ':\t', i[1])

age = 22
shekels = 3.46
print(shekels+age)

# F
phone = input("PLEASE INSERT YOUR PHONE NUMBER: ")
print("YOUR PHONE NUMBER IS :" + phone)

# G
def print_hello():
    print("hello")
print_hello()

def calculate():
    print(5 + 3.2)
calculate()

# H

def name():
    n = input("please insert your name: ")
    print("hii " + n)
name()

def number():
    numb = int(input("please insert your number:"))
    print(f" your number is : {numb/2}")
number()

# I

def uwu():
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    sum = float(num1) + float(num2)
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

def greeting(name, course):
    print ('welcome' ' ' + name + ' ' 'to' ' '+ 'the ' + course)

greeting('Stacie', 'python')






