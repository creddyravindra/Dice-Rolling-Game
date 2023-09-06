import random

def roll_dice():
    min_value = 1  # Minimum value on a dice
    max_value = 6  # Maximum value on a dice
    
    return random.randint(min_value, max_value)

def apply_obstacle(player_score):
    obstacle = random.choice(["lose_turn", "penalty"])
    
    if obstacle == "lose_turn":
        print("Oh no! You hit a lose a turn obstacle. Your turn is skipped.")
    elif obstacle == "penalty":
        penalty_amount = random.randint(1, 3)
        print(f"Oops! You encountered a penalty obstacle. You lose {penalty_amount} points.")
        player_score -= penalty_amount
    
    return player_score

def main():
    player1_score = 0
    player2_score = 0
    target_score = 100
    obstacle_count = random.randint(5, 10)  # Randomly determine the number of obstacles
    
    print(f"Welcome to the Dice Rolling Game with Obstacles! The first player to reach a score of {target_score} wins.")
    
    while player1_score < target_score and player2_score < target_score:
        # Player 1's turn
        input("Player 1, press Enter to roll the dice...")
        result = roll_dice()
        print(f"Player 1 rolled a {result}!")
        
        # Apply obstacle to Player 1 randomly
        if obstacle_count > 0 and random.choice([True, False]):
            player1_score = apply_obstacle(player1_score)
            obstacle_count -= 1
        
        player1_score += result
        print(f"Player 1's current score: {player1_score}")
        
        if player1_score >= target_score:
            print("Player 1 wins!")
            break
        
        # Player 2's turn
        input("Player 2, press Enter to roll the dice...")
        result = roll_dice()
        print(f"Player 2 rolled a {result}!")
        
        # Apply obstacle to Player 2 randomly
        if obstacle_count > 0 and random.choice([True, False]):
            player2_score = apply_obstacle(player2_score)
            obstacle_count -= 1
        
        player2_score += result
        print(f"Player 2's current score: {player2_score}")
        
        if player2_score >= target_score:
            print("Player 2 wins!")

if __name__ == "__main__":
    main()



