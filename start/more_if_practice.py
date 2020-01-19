price = 1000000

good_credit = input("did client have good credit??")

if "y" in good_credit:
    print("price is $" + str(0.8 * price))
else:
    print("price is $" + str(0.9 * price))

print("------------- OR , AND -----------------")

has_high_income = input("is income is high")
has_good_credit = input("is credit is good")

if "y" in has_good_credit:
    has_good_credit = True
else:
    has_good_credit = False

if "y" in has_high_income:
    has_high_income = True
else:
    has_high_income = False

if has_good_credit and has_high_income:
    print(f"price is $ {price * 0.8}")
elif has_good_credit or has_high_income:
    print(f"price is $ {price * 0.9}")
else:
    print(f"price is $ {price} ")

print("------------------ NOT  ----------------------------")

if not has_high_income:
    print("The income is low or medium")

if not has_good_credit:
    print("The credit is low or medium")
