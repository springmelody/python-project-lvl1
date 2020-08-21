#!/usr/bin/env python3
"""Brain prime game."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Run prime."""
    engine.play_game(prime)


if __name__ == '__main__':
    main()
