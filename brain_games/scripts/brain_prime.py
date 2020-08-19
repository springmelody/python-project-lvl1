#!/usr/bin/env python3
"""Brain prime game."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Run function."""
    engine.play_game(prime.DESCRIPTION, prime.get_game_data)


if __name__ == '__main__':
    main()
