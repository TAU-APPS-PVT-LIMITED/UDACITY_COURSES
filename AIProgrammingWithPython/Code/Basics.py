# Example of various arithmetic operators
num = 5
print("Initial value of num is: ", num)
num += 5
print("updated value of num", num)
num = num + 5
print("updated value of num", num)
num = num - 1
print("updated value of num", num)
num -= 2
print("updated value of num", num)
num *= 2
print("updated value of num", num)
num /= 2
print("updated value of num", num)
num **= 2  # "**" Exponentiation (note that ^ does not do this operation, as you might have seen in other languages)
print("updated value of num", num)
num //= 3  # "//" Divides and rounds down to the nearest integer
print("updated value of num", num)

num1 = 22
num2 = num1 + 5.0
print(num2)  # Anytime int + float operation is done, implicitly result is converted/promoted to float.
print(22 / 7)  # 3.142857142857143
print(type(num2))  # <class 'float'>

name = "Gaurav's Dam Robot"
print(type(name))
print(name[:3])  # Gau is printed. characters taken upto n-1 index where n is indexed subscript.
print(name[4:3])  # no output
print(name[5:])  # "v's Dam Robot" printed. Start from location n and until end
print(name[4:len(name)])  # "av's Dam Robot"
print(len(name))
# Traceback (most recent call last):
#   File "/Users/experimentalist/TRAINING/MYZEN/UDACITY/Intro2PythonProgramming/Code/Basics.py", line 34, in <module>
#     print(name[len(name)])
# IndexError: string index out of range
# Following line throws the above error. Reason being index is out of range, to get the 18th character,
# index should be 17th (n-1)
# print(name[len(name)])

marvel_universe = "Dr Strange rocks!!!."
no_one_matches_rdj = "RDJ is the greatest of all!! "
print(marvel_universe + no_one_matches_rdj)
print(no_one_matches_rdj * 4)
# print(len(4444)) #  object of type 'int' has no len()


"""
    Most common string methods examples

"""
print(marvel_universe.capitalize())
print(marvel_universe.upper())
print("My name is {} and I am a {}".format("Gaurav", "Software Architect"))

# split method
print(marvel_universe.split(' ', 2))  # ['Dr', 'Strange', 'rocks!!!.'] <= max split is 3 at ' '

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust " \
        "yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be " \
        "tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating," \
        "\n  And yet don’t look too good, nor talk too wise:"
print(verse)

count = len(verse)
print(count)
print(verse.count("you"))
print(verse.find("and"))
print(verse.rfind("you"))  # returns the highest index
