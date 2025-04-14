command = ""


while command.lower() != "stop":
    command = input(">").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped")
    elif command == "help":
        print("""
              start - to start the car
              stop - to stop the car
              quit - to quit
            """)
    else:
        "Sorry I don't Understand the command"