def monday():
    print("Hello world!")
    name = input("What's your name?")

    answer = input("Do you like mondays, " + name + "?")

    if answer == "yes":
        print("You're wrong, stop that...")
    elif answer == "no":
        print("I am too")
    else:
        print("What?")

monday()
