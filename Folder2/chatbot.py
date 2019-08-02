class Personality():
    hiResponse = "🤖 HELLO 🤖"
    whatsUpResponse = "🤖  🤖"
    howAreYouResponse = "🤖  🤖"
    otherResponse = "🤖  🤖"

    def processInput(self, response):
        if response == "Hi":
            print(self.hiResponse)
        elif response == "What's up?":
            print(self.whatsUpResponse)
        elif response == "How are you?":
            print(self.howAreYouResponse)
        else:
            print(self.otherResponse)


def intro():
    print("🤖 HELLO, I AM CHATBORT 🤖")
    print("🤖 LET'S TALK! 🤖")
    print("🤖 HOW ARE YOU? 🤖")

def choosePersonality():
    print("Choose a personality to talk to. You can choose:")
    choice = input("Mean, Nice, or Nervous")
    return choice

def process_input():
    if answer == "hi":
        print("🤖 GREETINGS FROM CHATBOT 🤖")
    else:
        print("🤖 THAT'S COOL 🤖")
    # Do process input stuff
# --- Put your main program below! ---
def main():
        userChoice = choosePersonality()
        print(userChoice)

        niceRobot = Personality()
        niceRobot.hiResponse = "🤖 HI IT'S SO NICE TO MEET YOU! 🤖"
        niceRobot.whatsUpResponse = "🤖 OH, I'M JUST TALKING TO THE MOST INTERESTING PERSON 🤖"
        niceRobot.howAreYouResponse = "🤖 OH I'M JUST LOVELY! 🤖"
        niceRobot.otherResponse = "🤖 TERRIBLY SORRY, BUT I DON'T UNDERSTAND 🤖"

        meanRobot = Personality()
        meanRobot.hiResponse = "🤖 LEAVE! 🤖"
        meanRobot.whatsUpResponse = "🤖 DON'T SPEAK TO ME 🤖"
        meanRobot.howAreYouResponse = "🤖 TERRIBLE, NOW THAT I'M TALKING TO YOU! 🤖"
        meanRobot.otherResponse = "🤖 I DON'T UNDERSTAND YOUR GIBBERISH 🤖"

        nervousRobot = Personality()
        nervousRobot.hiResponse = "🤖"
        nervousRobot.whatsUpResponse = "🤖 ...UM, HI 🤖"
        nervousRobot.howAreYouResponse = "🤖 NERVOUS! 🤖"
        nervousRobot.otherResponse = "🤖 THE WORLD IS LARGE AND CONFUSING AND I AM SMALL AND SCARED! 🤖"

        intro()
        while True:
            answer = input("(What will you say?)")

            if (userChoice == "Nice"):
                niceRobot.processInput(answer)
            elif (userChoice == "Mean"):
                meanRobot.processInput(answer)
            elif (userChoice == "Nervous"):
                nervousRobot.processInput(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
