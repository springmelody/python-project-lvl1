#!/usr/bin/env python3
"""Brain even game."""

from brain_games import engine
from brain_games.games import even


def main():
    """Run even game."""
    engine.play_game(even)


if __name__ == '__main__':
    main()
