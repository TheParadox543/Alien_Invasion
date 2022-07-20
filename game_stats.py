import json

from settings import Settings

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings:Settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # File for storing high score.
        self.file_high_name = "high_score.json"

        # Initializing the highscore.
        self._read_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score(self):
        """Initialize the high score from the file if file exists."""
        try:
            with open(self.file_high_name, 'r') as file:
                high_score:int = json.load(file)
        except FileNotFoundError:
            high_score = 0
        self.high_score = high_score

    def write_high_score(self):
        """Write the high score into the file on closing the game."""
        with open(self.file_high_name, 'w') as file:
            json.dump(self.high_score, file)