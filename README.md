# Snake Game

This project implements the classic Snake Game using Python's `turtle` module.

## Overview

In this game, the player maneuvers a snake to eat food cubes on the screen. Each time the snake eats a food cube, it grows in length, and the score increases. The game ends if the snake collides with the wall or itself.

## Features

- Control the snake using the arrow keys.
- The game keeps track of the score.
- The snake grows longer each time it eats the food.
- Simple and colorful graphical interface.
- Option to quit the game gracefully by pressing 'q'.

## Files

- `main.py`: The main script that runs the game.
- `snake.py`: Defines the `Snake` class, which contains methods to move the snake, extend its length, and check for collisions.
- `food.py`: Defines the `Food` class, which randomly places food on the screen.
- `scoreboard.py`: Defines the `Scoreboard` class, which updates and displays the score.

## Installation

1. Ensure you have Python 3.x installed.
2. Clone the repository.
3. Navigate to the project directory.

```bash
git clone <repository_url>
cd <project_directory>
```

4. Run the game.

```bash
python main.py
```

## How to Play

- Run the script `main.py`.
- Use the arrow keys to move the snake:
  - Up: ⬆
  - Down: ⬇
  - Left: ⬅
  - Right: ➡
- Press 'q' to quit the game at any time.

## Requirements

- `turtle` (standard Python library)

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspired by the classic Snake Game.
- Built using Python's `turtle` module.