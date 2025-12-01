# 01-Rock-Paper-Scissors

This project is a Python-based implementation of the popular game "Rock, Paper, Scissors". It provides the opportunity to play the game against a computer, which makes its moves based on random choice. The project is a meaningful exercise for those who already grasp the Python basics and want to dive into something more challenging and hands-on.

## How to Play

1. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```

2. Enter your choice when prompted: `rock`, `paper`, or `scissors`

3. The computer will randomly select its choice

4. The winner is determined by the classic rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock

5. Type `quit` to exit the game and see your final score

## Running Tests

To run the tests:
```bash
python -m unittest test_rock_paper_scissors -v
```

## Project Structure

- `rock_paper_scissors.py` - Main game implementation
- `test_rock_paper_scissors.py` - Unit tests for the game logic
- `README.md` - This file
- `LICENSE` - MIT License
