#!/usr/bin/env python3
"""Brain progression game."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Run function."""
    engine.play_game(progression.DESCRIPTION, progression.get_game_data)


if __name__ == '__main__':
    main()
