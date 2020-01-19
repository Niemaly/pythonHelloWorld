i = 1

while i<=5:
    print("*" * i)
    i+=1
print("done")


print("----------------- start stop and quit game --------------------")

run = True
started = False

while run:
    command = input("write what car should do, you can 'start' engine, 'stop' and 'quit' game\n")
    if command == "start" and started is False:
        print("Car started")
        started = True
        continue
    elif command=="start" and started is True:
        print("Car already started!!")
        continue
    elif command == "stop" and started is True:
        print("Car stopped")
        started = False
        continue
    elif command == "stop" and started is False:
        print("Car already stop!!")
        continue
    elif command == "quit":
        print("Quit game")
        run = False
    else:
        print("I don't understand command.")
        continue
