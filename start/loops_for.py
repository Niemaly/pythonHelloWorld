for item in "Jacek":
    print(item)

for item in ["Jacek", "Paweł", "Agata"]:
    print(item)

for item in range(50, 101, 5):
    print(item)

print("--------------------------- sum of prices exercises ----------------------------")

prices = [10, 20, 30]
total_price = 0

for item in prices:
    total_price += item

print(f"total price = {total_price}")

print("------------------------  points ex -----------------------------------------------")
for x in range(3):
    for y in range(3):
        print(f"x = {x}, y = {y}")

print(" ---------------------------- exercise -----------------------------------")
array = [5, 2, 5, 2, 2]

for item in array:
    print(item * "x")

print("-------------------------- now we draw L  -------------------------------")
array = [2, 2, 2, 2, 5]

for item in array:
    for string in item:
        string
