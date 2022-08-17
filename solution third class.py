# 1 + 2
try:
     a = 1/0
except:
    print("Division by zero")

# 3 - YES . ITS LEGAL , try can be with except, else and finally.
try:
    x = 1
finally:
    print("finally")


# 4 - all types of exceptions

# 5 - חסר חלק מהשאלה

# 6
# except ZeroDivisionError - cant divine in zero
# except IOError - I/O (input/output) exceptions

# 7
f = open("word.txt", "a")

# 8
f.write("mimi and michael")
f.close()

# 9
f = open("word.txt", "r")
print(f.read())

# 10
hebrew = "בראשית ברא אלהים את השמים ואת הארץ"
with open('unicode.txt', 'w', encoding='utf-8') as israeli:
    israeli.write(hebrew)
with open('unicode.txt', encoding='utf-8') as israelis:
    print(israelis.read())

# 11
from PIL import Image

img = Image.new('RGB', (60, 30), color=(73, 109, 137))
img.save('blue.png')
