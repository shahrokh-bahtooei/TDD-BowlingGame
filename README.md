# TDD-BowlingGame

Robert C. Martin (Uncle Bob) has shown test-driven development impressively through a nice Java demo. He has made a powerpoint document years ago to illustrate his example on TDD, known as [Bowling Game Kata](./Bowling%20Game%20Kata.ppt) over the web. He has also made a brilliant video recently under his *Clean Code* series which can be purchased at [Clean Coders](https://cleancoders.com/episode/clean-code-episode-6-p2/show). Here, with the help of Git Commit feature that can be taken advantage to follow step by step differences on codes easily on GitHub, a Python tutorial is created for TDD through the bowling game example based on built-in *unittest* module. As a better sample for Python unit testing, it extends the example to also address invalid usages.

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

The challenge is to develop a class to compute the final score gained in a bowling game by a test-first approach that leads to thorough tests and clean code. The resulted *Game* class should have two methods: *Roll* that is used to give fallen pins on each roll, and *Score* that is called at the end of the game to get the final score.

## Solution
To develop test-driven is to round in a simple cycle:  
1. ![RED][red] &nbsp;&nbsp;&nbsp; Test &nbsp;&nbsp; ![RED][red]  
   To write a test that implies one of the program logics. This should start with the simplest logic, and go to a bit complicated ones at next rounds. As there is no production code for the feature at the time, it should **fail**.  
2. ![GREEN][green] &nbsp;&nbsp; Code &nbsp; ![GREEN][green]  
   To write the minimum amount of production code just to **pass** the failing unit test, and not further.     
3. ![BLUE][blue] Refactor ![BLUE][blue]  
   To restructure both test code and production code into clean ones.
   
[red]: https://placehold.it/15/f03c15/000000?text=+ 
[green]: https://placehold.it/15/49E20E/000000?text=+
[blue]: https://placehold.it/15/1589F0/000000?text=+

This example is on two files, *test_bowling_game.py* and *bowling_game.py*, each one contains test code and production code, respectively. By navigating to the **commits** section, developing both files through rounding in the mentioned cycle is shown by each commit for every step. To start, open *Initial Commit* on a new tab and repeat for the next ones to see the difference.  
(Note that up to step 7-1, commits illustrate TDD cycle. Afterwards, they are used normally for each improvement to the code seeking to handle misuses.)

