"""Generate pencil color names by randomly combining names from 2 separate lists."""
import random
import sys

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("\nWelcome to Colors 2.\nNavy blue? Light cyan? BORING.\nThe colors of the future will be named using a random generator.\n\n")
    print("Here's a brand new color name:")

    first = ("mighty", "imperfect", "ugly", "spooky", "watery",
    "discreet", "narrow", "ultra", "therapeutic", "flat", "funny",
    "slimy", "damp", "cuddly", "pale", "troubled", "silent",
    "flimsy", "wiggly", "clammy")

    last = ("black", "gray", "maroon", "red", "purple", "fuschia",
    "green", "lime", "yellow", "blue", "teal", "aqua")

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        #Trick IDLE by using "fatal error" setting to print name in red.
        print(f"{first_name} {last_name}", file=sys.stderr)

        try_again = input("Try again? (Press Enter to try again or n to quit)\n")
        if try_again.lower() == "n":
            break

    input("Press Enter to exit. Thank you for playing.")

if __name__ == "__main__":
    main()
