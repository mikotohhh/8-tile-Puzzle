# 8-tile-Puzzle
You solve the puzzle by moving the tiles around. 
For each step, you can only move one (not more!) of the neighbor tiles (left, right, top, bottom but not diagonally) into an empty grid. 
And all tiles must stay in the 3x3 grid (so no wrap around allowed). 
An example is shown in the picture below. Suppose we start from the following configuration:

<img width="867" alt="Screen Shot 2022-10-15 at 21 59 17" src="https://user-images.githubusercontent.com/112918739/196015903-2c31f921-4270-4fda-a3ca-e1eb3cfd3c58.png">
That is, in the above example, we would either move 3 or 6 down or move 7 to the right. Given these rules for the puzzle, we will generate a state space and solve this puzzle using the A* search algorithm.
