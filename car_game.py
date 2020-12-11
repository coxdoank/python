command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car Started ...")
    elif command == "stop":
        if not started:
            print("Car Already Stop")
        else:
            started = False
            print("Car Stopped ...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry, I don't understand the command")