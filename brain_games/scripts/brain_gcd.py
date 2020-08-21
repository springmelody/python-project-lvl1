#!/usr/bin/env python3
"""Brain gcd game."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Run gcd game."""
    engine.play_game(gcd)


if __name__ == '__main__':
    main()
