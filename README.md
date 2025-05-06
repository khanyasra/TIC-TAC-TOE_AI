# TIC-TAC-TOE_AI: Minimax vs Alpha-Beta Pruning
This project implements a Tic-Tac-Toe game with two AI players using the Minimax algorithm and its optimization via Alpha-Beta Pruning. The goal of this project is to explore and compare the performance of both algorithms in making optimal moves in the game.

Features
Tic-Tac-Toe Game Logic: Implements the core logic of the Tic-Tac-Toe game, including player turns, win detection, and game state updates.

Minimax Algorithm: The AI player using Minimax makes optimal decisions by evaluating all possible game states recursively.

Alpha-Beta Pruning: This optimization improves the efficiency of the Minimax algorithm by pruning branches of the game tree that cannot influence the final decision.

Performance Comparison: The execution time of both algorithms (Minimax and Alpha-Beta Pruning) is measured and displayed to highlight the difference in efficiency.

Algorithms Used
Minimax Algorithm (for player X):

A recursive algorithm that evaluates all possible future states of the game and selects the move that maximizes player X’s chances of winning.

It searches the entire game tree and uses the concepts of maximizing and minimizing moves to select the best option.

Alpha-Beta Pruning (for player O):

An optimization technique for the Minimax algorithm that cuts off branches in the game tree which cannot affect the final decision, significantly reducing the number of nodes evaluated.

This allows the AI to make decisions faster while still maintaining optimal play.

How It Works
The game starts with an empty 3x3 board.

Player X uses the Minimax algorithm to make its move, and Player O uses Alpha-Beta Pruning.

Each move is evaluated based on the possible future states, and the optimal move is selected by the respective algorithm.

The game continues until a player wins, or all spaces are filled (resulting in a draw).

The execution time for each move is displayed, allowing you to compare the efficiency of the two algorithms.
