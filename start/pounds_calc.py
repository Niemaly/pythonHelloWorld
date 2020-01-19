run = True

weight = int(input("what is your weight?\n"))

print(weight)

kg_or_pounds = input("(L)bs or (K)g\n")

if kg_or_pounds == "K":
    converted = weight/0.45
    print(f"your weight is: {converted} lbs")
elif kg_or_pounds == "L":
    converted = weight*0.45
    print(f"your weight is: {converted} kg")