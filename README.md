# Mem_box_game
Memory Obstacle Game
Brief Overview:
The Memory Obstacle Game is a Python-based memory and reflex game built using Pygame. Players must memorize obstacle blocks, then avoid selecting them while clicking on all other blocks. As levels increase, the difficulty rises with fewer obstacle blocks and shorter memorization phases.

Features
Dynamic Gameplay:
Each level generates a new grid with randomly placed obstacle blocks.
The difficulty increases as the number of obstacle blocks decreases.
Memorization Phase:
Players are given a few seconds to memorize the obstacle blocks, highlighted in red.
Player Interaction:
Click on all safe blocks (non-obstacle blocks) to progress to the next level.
If an obstacle block is clicked, the game resets.
Score and Levels:
Scores are incremented for each successfully completed level.
Levels increase, and the challenge grows dynamically.
No Fixed End:
The game continues until the player clicks an obstacle block.

Controls:
S Key: Start or restart the game.
R Key: Restart the game from level 1.
E Key: Exit the game.
Mouse Click: Select blocks during the gameplay phase.

Modules Required
Before running the game, ensure you have the following Python modules installed:
Pygame:
Installation:
bash
Copy code
pip install pygame
Random (Standard Library):
No installation needed; part of Python’s standard library.
Time (Standard Library):
Used for delays and managing the memorization phase.

How to Play
Start the Game: Press the S key to start.
Memorize Obstacles: Red blocks appear for 3 seconds. Memorize their positions.
Select Safe Blocks: Click on all blocks except the obstacle blocks.
Level Progression: Successfully select all safe blocks to move to the next level.
Avoid Obstacles: If you click on an obstacle block, the game resets to level 1.
Exit: Press E to quit the game.

Technical Details
Grid Dimensions:
The grid is a 4x4 matrix.
Each block size is dynamically calculated based on the screen size.
Obstacle Count:
The number of obstacles reduces as the level increases.
This creates a balance between difficulty and engagement.
Game Loop:
The game continuously refreshes the screen to handle events and updates.
Reset Logic:
If an obstacle is selected, the score and level reset, and new obstacles are generated.

How to Run
Install Python (3.7+ recommended).
Install Pygame using pip install pygame.
Save the code to a file, e.g., memory_obstacle_game.py.
Run the script using:
bash
Copy code
python memory_obstacle_game.py

Future Enhancements
Dynamic Grid Size: Increase grid size for advanced levels.
Leaderboard System: Save high scores locally or online.
Sound Effects: Add audio feedback for clicks, level-ups, and game-over events.
Customization: Allow players to adjust difficulty levels or grid size.
