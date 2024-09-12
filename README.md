
# BombParty Auto-Player

This Python script automates playing BombParty by identifying and typing the best possible words that contain the specified letters. The script utilizes a dictionary and optimizes word selection based on specific criteria.

## Features
- Automatically identifies words containing the given letters.
- Selects the word with the most "useful" letters (configurable).
- Switches to the BombParty window, types the word, and submits it.
- Uses multiple dictionaries for better word variety (`dict.txt`, `enable.txt`, `moby.txt`).

## How it Works
1. The script loads words from several dictionary files (`dict.txt`, `enable.txt`, `moby.txt`).
2. You input the letters that must be contained in the word.
3. The script finds matching words and selects the optimal one based on the most available letters.
4. It automatically switches to the BombParty window, types the selected word, and presses enter.

## Requirements

- Python 3.x
- `keyboard` library
  ```bash
  pip install keyboard
  ```
- A dictionary file (`dict.txt`) with a list of valid words.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bombparty-auto-player.git
   cd bombparty-auto-player
   ```
2. Ensure you have dictionary files named `dict.txt`, `enable.txt`, and `moby.txt`. Place them in the root directory.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Usage

1. Run the script.
2. When prompted, input the letters you want to be included in the word.
3. The script will automatically switch to the BombParty window, enter the word, and submit it.

### Example

```
What letters to contain: tr
```

The script will find words that contain "tr", such as "train", "treat", etc., and automatically enter the best word in BombParty.

## Customization

You can modify the script to:
- Change the criteria for selecting the best word.
- Adjust the timing of window switching and word typing.
- Add or modify the dictionary files to improve word variety.
