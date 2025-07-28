# 🧠PLAYBLOCK - Memory Obstacle Game

A sleek memory-based puzzle game built using **Pygame**. The objective is to **memorize obstacle positions**, and then avoid clicking them under pressure. The difficulty ramps up with every level — less time to memorize, more obstacles to dodge!

---


## 🚀 How to Play

1. **Memorize the red blocks** when the grid appears briefly.
2. After the flash, start clicking the **safe tiles** (non-obstacles).
3. Avoid clicking red block positions — or it's **Game Over**!
4. Complete the safe tiles to move to the **next level**.

> 🧠 The game gets faster and trickier with every level.

---

## 🛠️ Features

- ✅ Modern, clean UI with soft shadows
- ✅ Increasing difficulty with level progression
- ✅ Memorize → Click phase transition
- ✅ Game Over and Victory screen with restart
- ✅ Animated time bar and scoring
- ✅ Responsive design using constants
- ✅ Fully built from scratch without external UI libraries

---

## 🧩 Controls

| Action         | Input          |
|----------------|----------------|
| Select Tile    | Mouse Click    |
| Restart Game   | Mouse Click on Game Over screen |
| Quit Game      | Close Window or `ESC` |

---

## 💻 Run the Game Locally

### Prerequisites

- Python 3.7+
- [Pygame](https://www.pygame.org/)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/yourusername/memory-obstacle-game.git

# Navigate into the folder
cd memory-obstacle-game

# Install dependencies
pip install pygame

# Run the game
python main.py
