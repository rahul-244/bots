# Bots Repository

Welcome to the Bots repository where I develop and share automated bots for various games. These bots are designed to automate tasks within the games to enhance performance and efficiency.

## Magic Tile Bot

The Magic Tile Bot is an automation script that helps players achieve higher scores in the Magic Tiles game by detecting and clicking the correct tiles as they appear. 
This bot is designed to interact with the game using the Python libraries `pyautogui`, `keyboard`, and `win32api`.

### How It Works

The bot operates by continuously scanning a fixed area of the screen where tiles appear in the game. When it detects a black tile (a tile that needs to be clicked), it performs a mouse click at the tile's location. 
The bot runs until the 'q' key is pressed, allowing for easy termination of the script.

### Dependencies

To run the Magic Tile Bot, you need to install the following Python libraries:

- `pyautogui`
- `keyboard`
- `win32api`

You can install these dependencies via pip:

bash
pip install pyautogui keyboard pywin32

### Usage

Start the Magic Tiles game and align it on your screen according to the coordinates specified in the bot script.
Run the script in your Python environment.
Press 'q' to stop the bot when you are done.

### Safety Notice

Please note that using bots can violate the terms of service of some games. Use this bot at your own risk.

### Contributing

Interested in contributing to the Bots repository? Great! Feel free to fork the repository, make changes, and submit a pull request.

### Acknowledgments

Game information and inspiration from Magic Tiles

### Contact

If you have any suggestions or questions, feel free to open an issue on this repository.
