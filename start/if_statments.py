is_hot = input("is it hot tooday")

if "yes" in is_hot:
    is_hot = bool(True)
else:
    is_hot = bool(False)

if is_hot:
    print("it is a hot day")
    print("plz take some water with you")
else:
    print("its a cold day!")
    print("plz wear some warm cloths")
print("have a nice day")

