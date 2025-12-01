"""
Tests for Rock, Paper, Scissors Game
"""

import unittest
from unittest.mock import patch

from rock_paper_scissors import (
    VALID_CHOICES,
    get_computer_choice,
    determine_winner,
)


class TestComputerChoice(unittest.TestCase):
    """Tests for the get_computer_choice function."""

    def test_computer_choice_is_valid(self):
        """Test that computer choice is always a valid option."""
        for _ in range(100):
            choice = get_computer_choice()
            self.assertIn(choice, VALID_CHOICES)

    @patch('rock_paper_scissors.random.choice')
    def test_computer_choice_uses_random(self, mock_choice):
        """Test that get_computer_choice uses random.choice."""
        mock_choice.return_value = "rock"
        result = get_computer_choice()
        mock_choice.assert_called_once_with(VALID_CHOICES)
        self.assertEqual(result, "rock")


class TestDetermineWinner(unittest.TestCase):
    """Tests for the determine_winner function."""

    def test_tie_scenarios(self):
        """Test that identical choices result in a tie."""
        for choice in VALID_CHOICES:
            result = determine_winner(choice, choice)
            self.assertEqual(result, "tie", f"{choice} vs {choice} should be tie")

    def test_rock_beats_scissors(self):
        """Test that rock beats scissors."""
        result = determine_winner("rock", "scissors")
        self.assertEqual(result, "win")

    def test_scissors_beats_paper(self):
        """Test that scissors beats paper."""
        result = determine_winner("scissors", "paper")
        self.assertEqual(result, "win")

    def test_paper_beats_rock(self):
        """Test that paper beats rock."""
        result = determine_winner("paper", "rock")
        self.assertEqual(result, "win")

    def test_scissors_loses_to_rock(self):
        """Test that scissors loses to rock."""
        result = determine_winner("scissors", "rock")
        self.assertEqual(result, "lose")

    def test_paper_loses_to_scissors(self):
        """Test that paper loses to scissors."""
        result = determine_winner("paper", "scissors")
        self.assertEqual(result, "lose")

    def test_rock_loses_to_paper(self):
        """Test that rock loses to paper."""
        result = determine_winner("rock", "paper")
        self.assertEqual(result, "lose")

    def test_invalid_player_choice_raises_error(self):
        """Test that invalid player choice raises ValueError."""
        with self.assertRaises(ValueError):
            determine_winner("invalid", "rock")

    def test_invalid_computer_choice_raises_error(self):
        """Test that invalid computer choice raises ValueError."""
        with self.assertRaises(ValueError):
            determine_winner("rock", "invalid")


class TestValidChoices(unittest.TestCase):
    """Tests for VALID_CHOICES constant."""

    def test_valid_choices_contains_required_options(self):
        """Test that VALID_CHOICES contains rock, paper, and scissors."""
        self.assertIn("rock", VALID_CHOICES)
        self.assertIn("paper", VALID_CHOICES)
        self.assertIn("scissors", VALID_CHOICES)

    def test_valid_choices_length(self):
        """Test that VALID_CHOICES has exactly 3 options."""
        self.assertEqual(len(VALID_CHOICES), 3)


if __name__ == "__main__":
    unittest.main()
