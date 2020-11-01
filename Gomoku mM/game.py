from ui import Console

def main():
    while True:
        print(" 1.Console   ")
        print(" 2.GUI       ")
        chosenUi = input("Choose interface:")
        if chosenUi == "1":
            game = Console()
            game.run()
        elif chosenUi == "2":
            pass
        else:
            print("Invalid option!")

main()