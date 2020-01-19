hello_world = "Hello World"
print(hello_world[0] + hello_world[1] + hello_world[2] + hello_world[3] + hello_world[4] + hello_world[5])
print(hello_world[-1] + hello_world[-2] + hello_world[-3] + hello_world[-4] + hello_world[-5] + hello_world[-6])
print(hello_world[0:5])
print("-------------------------------------------")
another = hello_world[:]
print("this is a clone of string "+ another)

print(hello_world[1:-1])

print("--------------------------------------------")

name = "jacek"
name2 = name
name += " Szumski"
print(name + '  ' + name2)


print('-------- formated strings ------------------')

name = "jacek"
surname = "Szumski"
massage = name + " ['" + surname + "'] " + "is a coder"

formatted_massage = f"{name} ['{surname}'] is a coder"

print(massage)
print(formatted_massage)

print("------------ length of strings ---------------")

print(len(formatted_massage))


print("-------------- string methods ---------------")

string = "Custom String"

print(string.index("u"))
print(string.upper())
print(string.capitalize())
print(string.find("i"))
print(string.replace("String", "Fantastic String"))
print("String" in string)
print(string.title())

