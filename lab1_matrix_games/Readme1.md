# Laboratory Work 1: Conflict Situations and Matrix Games

This directory contains the solution for the first laboratory work of the "Game Theory" course. The work is focused on modeling conflict situations using payoff matrices and analyzing zero-sum games in pure strategies.

## Task (Variant 5)
Analysis of 6 payoff matrices of dimension 3×4 (with element values in the range `[-4, 5]`). For each matrix, the algorithm determines:
- The lower value of the game (maximin) and the maximin (defensive) strategy of Player 1.
- The upper value of the game (minimax) and the minimax (defensive) strategy of Player 2.
- The coordinates of the saddle points (if a solution in pure strategies exists).

The matrices are divided into three categories:
1. Having more than one saddle point.
2. Having exactly one saddle point.
3. Having no saddle points (requiring a transition to mixed strategies).

## Structure 
- `main.py` — Python script for automatic calculation of game parameters and saddle point detection.
- `lab1_report.pdf` — Detailed report containing theoretical calculations and results analysis.

## Usage
The script is written in pure Python and requires no external dependencies.

```bash
python main.py