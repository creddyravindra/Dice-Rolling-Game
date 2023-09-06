import random

def roll_dice():
    min_value = 1  
    max_value = 6  
    
    return random.randint(min_value, max_value)

def main():
    player1_score = 0
    player2_score = 0
    target_score = 100
    
    print(f"Welcome to the Two Player Dice Rolling Game! The first player to reach a score of {target_score} wins.")
    
    while player1_score < target_score and player2_score < target_score:
        input("Player 1, press Enter to roll the dice...")
        result = roll_dice()
        print(f"Player 1 rolled a {result}!")
        player1_score += result
        print(f"Player 1's current score: {player1_score}")
        
        if player1_score >= target_score:
            print("Player 1 wins!")
            break
        
        input("Player 2, press Enter to roll the dice...")
        result = roll_dice()
        print(f"Player 2 rolled a {result}!")
        player2_score += result
        print(f"Player 2's current score: {player2_score}")
        
        if player2_score >= target_score:
            print("Player 2 wins!")

if __name__ == "__main__":
    main()
