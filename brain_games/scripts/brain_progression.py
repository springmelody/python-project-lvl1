#!/usr/bin/env python3
"""Brain progression game."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Run progression game."""
    engine.play_game(progression)


if __name__ == '__main__':
    main()
