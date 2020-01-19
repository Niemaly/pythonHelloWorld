run = True

while run:
    name = input("write your name, it must be longer than 3 characters and have less then 30 characters\n")

    if len(name) < 3:
        print("your name have less than 3 characters!!")
    elif len(name) > 50:
        print("your name is too long! It has to have less than 30 characters")
    else:
        print("your name is ok")
        print(f"welcome to our app mr {name}")
        run = False
