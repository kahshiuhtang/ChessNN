# ChessNN: Neural Network for playing chess

## Goal

I want the engine to be able to play at competitively at an ELO rating around 2000. Personally, I am no where near this level so I am not sure how feasible this goal is. An average club level chess player would have an ELO rating around 1500. At 2000 ELO, the lower rated player is only expected to win 5% of the time.

## Design

The goal of the neural network is to map an evaluation function f(X) where X is a chess position in the form.

<em>Opening</em>: Many openings have already been researched by the best grandmasters in the world. I believe for around 10 moves, there will be a given best move for a position. I will take the a database of openings and store them in a database and have the AI take from th

<em>Middlegame</em>: This is where I believe the neural network will be needed. I will need some sort of analyzer to evaluate a position, as I cannot trust myself to create this function. I don't think it will be easy to check patterns as the queens will still be on the board.

<em>Endgame</em>: Similar to the opening, I believe that there is repetition in the endgame. The engine will need to recognize patterns to end games. However, there should be enough pieces off the board to decrease the move tree to where this is feasible. However, the neural network will still need to be able to generate some best moves by itself in cases where there is an open board with many minor pieces still available.

## Sources

As expected, I had to find some sources to do research.
[Repository Source 1](https://github.com/lorenzenv/Neural-Network-Chess-Engine)

[Repository Source 2](https://github.com/pbaer/neural-chess)

[Repository Source 3](https://github.com/undera/chess-engine-nn)

## Data/Game

[Source 1](https://www.pgnmentor.com/files.html#openings)

[Source 2](http://caissabase.co.uk)

[Source 3](https://database.lichess.org/#standard_games)

<em> Players </em>

One thing I do not want to do is train with games from lower rated players. A lot of databases store games from players of a large range but I will focus on games player at the GM level mainly. I plan to have the

Some personal players that I like and would want the engine to "learn" from:

Mikhail Tal

Jose Raul Capablanca

Anatoly Karpov

Magnus Carlsen

Tigran Petrosian

Bobby Fischer

These players do not have a similar playstyle but instead excel in different aspects of the game. I am interested to see how the
