#!/usr/bin/env python3
"""Brain gcd game."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Run function."""
    engine.play_game(gcd.DESCRIPTION, gcd.get_game_data)


if __name__ == '__main__':
    main()
