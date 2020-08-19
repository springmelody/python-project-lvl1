#!/usr/bin/env python3
"""Brain calc game."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Run function."""
    engine.play_game(calc.DESCRIPTION, calc.get_game_data)


if __name__ == '__main__':
    main()
