#!/usr/bin/env python3
"""Brain even game."""

from brain_games import engine
from brain_games.games import even


def main():
    """Run function."""
    engine.play_game(even.DESCRIPTION, even.get_game_data)


if __name__ == '__main__':
    main()
