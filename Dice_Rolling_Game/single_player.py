import random

def roll_dice():
    min_value = 1  
    max_value = 6  
    
    return random.randint(min_value, max_value)

def main():
    play_again = "yes"
    
    while play_again.lower() in ["yes", "y"]:
        input("Press Enter to roll the dice...")
        
        result = roll_dice()
        
        print(f"You rolled a {result}!")
        
        play_again = input("Do you want to roll again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
