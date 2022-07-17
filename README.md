# TDD-BowlingGame

Test-driven-development is a good practice to write test code prior to production code. As Robert C. Martin shows it impressively through a slideshow on [Bowling Game Kata](./Bowling%20Game%20Kata.ppt) and a video on [Clean Coders](https://cleancoders.com/episode/clean-code-episode-6-p2/show), it comprises repeating a cycle of writing some test code that fails, developing some production code that passes the test, and refactoring on both sides. 

Using GitHub’s facility to monitor code changes over commits, this tutorial shows a step-by-step Python version of the bowling game example. As a more thorough sample, this repo extends the problem to address also invalid cases via exceptions.

## Problem
Here is a sample score table of a bowling player:

| Frame | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Rolls | 1 &nbsp;&nbsp; 4 | 4 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | 5 &nbsp;&nbsp; / | ✕ | 0 &nbsp;&nbsp; 1 | 7 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | ✕ | 2 &nbsp;&nbsp; / &nbsp;&nbsp; 6 |
|Score| 5 | 14 | 29 | 49 | 60 | 61 | 77 | 97 | 117 | **133** |

Rules of the game are as Robert explains in *Bowling Game Kata.ppt*:
>The game consists of 10 frames as shown above.  In each frame the player has two opportunities to knock down 10 pins.  The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.
>
>A spare is when the player knocks down all 10 pins in two tries.  The bonus for that frame is the number of pins knocked down by the next roll.  So in frame 3 above, the score is 10 (the total number knocked down) plus a bonus of 5 (the number of pins knocked down on the next roll.)
>
>A strike is when the player knocks down all 10 pins on his first try.  The bonus for that frame is the value of the next two balls rolled.
>
>In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame.  However no more than three balls can be rolled in tenth frame.

The challenge is to develop a class to compute the final score gained in a bowling game by a test-first approach that leads to thorough tests and clean code. The resulted *Game* class should have two methods: 

- *Roll:* Used to give fallen pins on each roll  
- *Score:* Called at the end of the game to get the final score

## Solution
To develop test-driven is to round in a simple cycle:  
1. [![Generic badge](https://img.shields.io/badge/⎍-Test-red.svg)](https://shields.io/)  
   To write a test that implies one of the program logics. This should start with the simplest logic and proceed toward slightly more complicated ones at next rounds. Because there is no production code for the feature at the time, it should **fail**.  
2. [![Generic badge](https://img.shields.io/badge/⎍-Code-brightgreen.svg)](https://shields.io/)  
   To write the minimum amount of production code just to **pass** the failing unit test, but not further.     
3. [![Generic badge](https://img.shields.io/badge/⎍-Refactor-blue.svg)](https://shields.io/)  
   To restructure both test code and production code into clean ones.  

The solution is on the two files *test_bowling_game.py* and *bowling_game.py*, where the former contains the test code and the latter has the production code. To see the development, please navigate to the **commits** section, where each commit up to *7-1*  reveals one step in the TDD cycle. To walk through the whole procedure, please start with opening *Initial Commit* on a new tab and proceed to the next ones.
