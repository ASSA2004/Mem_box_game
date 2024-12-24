# Mem_box_game
Brief Overview:
The Memory Obstacle Game is an interactive Python-based grid memory game built using the Pygame library. Players are challenged to memorize obstacle blocks within a limited time and select all other blocks correctly. The difficulty progressively increases as levels advance, keeping the game engaging and challenging.

Game Features:

Dynamic Gameplay: Each level introduces a new set of randomly generated obstacle blocks.
Memorization Phase: Players are given a brief period to memorize the positions of obstacle blocks.
Increasing Difficulty: As players advance, the number of obstacle blocks decreases, requiring better memory and focus.
Scoring System: Tracks player progress by increasing the score with each successful level completion.
Continuous Play: The game has no definitive end; players can keep progressing until they make a mistake.
Controls:

S Key: Start or restart the game.
R Key: Restart the game from level 1.
E Key: Exit the game.
Mouse Click: Select blocks during the gameplay phase.
How It Works:

Grid Display: The game starts with a 4x4 grid where each block is clickable.
Obstacle Highlighting: During the memorization phase, obstacle blocks are highlighted in red for 3 seconds.
Player Interaction: After memorization, all blocks are hidden, and players must select the safe blocks (non-obstacle blocks).
Feedback:
Selecting an obstacle block ends the game and resets progress.
Successfully selecting all safe blocks advances the player to the next level.
Technical Details:

Python Libraries: Pygame for graphical rendering and game loop handling.
Dynamic Difficulty: Uses a formula to adjust the number of obstacles as levels progress.
Responsive Grid: Automatically calculates block sizes based on the screen dimensions.
Future Enhancements:

Add sound effects for clicks and level-ups.
Introduce a timer for user input to increase tension.
Expand grid size for higher difficulty at advanced levels.
Implement a leaderboard system to save high scores.
