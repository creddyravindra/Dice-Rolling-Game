# Dice-Rolling-Game

This repository contains a simple dice rolling game implemented in Python. The game simulates the rolling of a six-sided die and allows players to accumulate scores based on their rolls.

## Table of Contents

- [Single Player Implementation](#single-player-implementation)
- [Two Player Implementation](#two-player-implementation)
- [Obstacles Added](#obstacles-added)
- [How to Play](#how-to-play)

## Single Player Implementation

The initial implementation of the game is a single-player version. In this version, a player can roll the dice as many times as they want.

## Two Player Implementation

In the second implementation, we expanded the game to support two players. Each player takes turns rolling the dice, and their scores are updated separately. The game continues until one of the players reaches a specified target score, usually 100 points. This version introduces friendly competition between two players.

## Obstacles Added

The final version of the game includes the concept of obstacles. Obstacles are challenges that players may encounter during their turns. There are two types of obstacles: "lose_turn" and "penalty." "Lose_turn" obstacles skip the player's turn, while "penalty" obstacles deduct a random number of points from the player's score. The number of obstacles and when they occur is determined randomly to add an element of unpredictability to the game.

## How to Play

To play the game, follow these steps:

1. Clone this repository to your local machine.
2. Run the Python script for the version you want to play: `single_player.py`, `two_player.py`, or `obstacles.py`.
3. Follow the on-screen prompts to roll the dice and make choices.
4. The game continues until a player wins or achieves a target score (for two-player and obstacle versions).

Enjoy the game and have fun rolling the dice!

Feel free to contribute to this project or provide feedback to improve the game.
