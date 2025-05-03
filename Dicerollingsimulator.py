# import random 

# def roll_dice():
#     # Ask the user how many dice they want to roll
#     num_dice = int(input("How many dice would you like to roll? "))

#     # Ask the user how many sides each die has
#     num_sides = int(input("How many sides does each die have? "))

#     # Roll the dice and store the results in a list
#     results = [random.randint(1, num_sides) for _ in range(num_dice)]

#     # Print the results
#     print("You rolled:", results)


import random

def get_valid_input(prompt, min_value=1):
    """Get validated integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def roll_dice(num_dice, num_sides):
    """Rolls num_dice dice with num_sides and returns a list of results."""
    return [random.randint(1, num_sides) for _ in range(num_dice)]

def show_summary(results):
    """Prints summary statistics for the rolled dice."""
    print("\n🎲 Dice Roll Summary:")
    print(f"Results: {results}")
    print(f"Total: {sum(results)}")
    print(f"Average: {sum(results) / len(results):.2f}")
    print(f"Highest Roll: {max(results)}")
    print(f"Lowest Roll: {min(results)}\n")

def ask_to_continue():
    """Asks the user if they want to roll again."""
    while True:
        choice = input("Would you like to roll again? (yes/no): ").strip().lower()
        if choice in ('yes', 'y'):
            return True
        elif choice in ('no', 'n'):
            return False
        else:
            print("Please enter yes or no.")

def main():
    print("🎲 Welcome to the Advanced Dice Roller!\n")

    while True:
        num_dice = get_valid_input("How many dice would you like to roll? ")
        num_sides = get_valid_input("How many sides does each die have? ")

        results = roll_dice(num_dice, num_sides)
        show_summary(results)

        if not ask_to_continue():
            print("Thanks for playing! Goodbye. 👋")
            break

if __name__ == "__main__":
    main()
